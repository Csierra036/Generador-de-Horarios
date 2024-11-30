from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from typing import Type, TypeVar, Generic, Optional, Dict, Any, List
from loguru import logger
from src.config import settings

# Declaración base para modelos de SQLAlchemy
Base = declarative_base()

# Definición de un tipo genérico para los modelos
ModelType = TypeVar("ModelType")


class CustomSQLAlchemyRepository(Generic[ModelType]):
    def __init__(self, db: Session, model: Type[ModelType]):
        """
        Inicializa el repositorio para un modelo específico y una sesión activa.
        """
        self.db = db
        self.model = model

    def get(self, id: int) -> Optional[ModelType]:
        """Obtiene un registro por ID."""
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self) -> List[ModelType]:
        """Obtiene todos los registros."""
        return self.db.query(self.model).all()

    def create(self, obj_in: Dict[str, Any]) -> ModelType:
        """Crea un nuevo registro."""
        obj_in = self._modify_document_before_insert(obj_in)
        new_obj = self.model(**obj_in)
        self.db.add(new_obj)
        self.db.commit()
        self.db.refresh(new_obj)
        return new_obj

    def update(self, db_obj: ModelType, obj_in: Dict[str, Any]) -> ModelType:
        """Actualiza un registro existente."""
        obj_in = self._modify_update_before_update(obj_in)
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> Optional[ModelType]:
        """Elimina un registro por ID."""
        obj = self.db.query(self.model).filter(self.model.id == id).first()
        if obj:
            self.db.delete(obj)
            self.db.commit()
        return obj

    def _modify_document_before_insert(self, document: Dict[str, Any]) -> Dict[str, Any]:
        """Lógica para modificar el documento antes de la inserción."""
        document["created_at"] = datetime.utcnow()
        document["updated_at"] = datetime.utcnow()
        return document

    def _modify_update_before_update(self, update: Dict[str, Any]) -> Dict[str, Any]:
        """Lógica para modificar los datos antes de la actualización."""
        update["updated_at"] = datetime.utcnow()
        return update


class DatabaseConnection:
    def __init__(self, database_url: str = settings.URL_DATABASE):
        """
        Inicializa la conexión a la base de datos.
        """
        self.engine = create_engine(database_url, pool_pre_ping=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        """Proporciona una sesión de base de datos."""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def setup_models(self):
        """Crea todas las tablas definidas en los modelos."""
        try:
            Base.metadata.create_all(self.engine)
            logger.info("Database tables created successfully.")
        except SQLAlchemyError as e:
            logger.error(f"Error creating tables: {e}")
            raise

    def teardown_models(self):
        """Elimina todas las tablas definidas en los modelos."""
        try:
            Base.metadata.drop_all(self.engine)
            logger.info("Database tables dropped successfully.")
        except SQLAlchemyError as e:
            logger.error(f"Error dropping tables: {e}")
            raise
