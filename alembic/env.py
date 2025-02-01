from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from src.database import Base
from dotenv import load_dotenv
import os
from src.models.academic_period import AcademicPeriod
from src.models.campus import Campus
from src.models.career_campus import CareerCampus
from src.models.career_period import CareerPeriod
from src.models.career_teacher import CareerTeacher
from src.models.career import Career
from src.models.classroom import Classroom
from src.models.course import Course
from src.models.hours import Hours
from src.models.modality import Modality
from src.models.room_block import RoomBlock
from src.models.section_teacher import SectionTeacher
from src.models.section_weeks import SectionWeeks
from src.models.section import Section
from src.models.teacher_time import TeacherTime
from src.models.teacher import Teacher
from src.models.time_block import TimeBlock
from src.models.week import Week

# Cargar variables de entorno desde .env
load_dotenv()
DATABASE_URL = os.getenv("URL_DATABASE")

if DATABASE_URL is None:
    raise ValueError(
        "La variable de entorno URL_DATABASE no está definida en el archivo .env"
    )

# Obtener configuración de Alembic
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configurar logging si se define en alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata para autogeneración de migraciones
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecuta las migraciones en modo offline."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta las migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
