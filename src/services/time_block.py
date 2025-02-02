from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Integer, DateTime
from datetime import datetime  # Si necesitas la clase estándar de Python
from src.database import CustomSQLAlchemyRepository
from src.models.time_block import TimeBlock, CreateTimeBlockRequest
from src.models.hours import Hours, CreateHoursRequest
from src.models.week import Week, CreateWeekRequest
from src.models.academic_period import AcademicPeriod, CreateAcademicPeriodRequest


class TimeBlockService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo TimeBlock y la sesión actual
        self.db_session = db_session
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=TimeBlock)
        self.week_repository = CustomSQLAlchemyRepository(db=db_session, model=Week)
        self.hours_repository = CustomSQLAlchemyRepository(db=db_session, model=Hours)
        self.academic_period_repository = CustomSQLAlchemyRepository(
            db=db_session, model=AcademicPeriod
        )

    def get_all_time_blocks(self):
        """Obtiene todos los bloques de tiempo."""
        return self.repository.get_all()

    def get_time_block_by_id(self, time_block_id: int):
        """Obtiene un bloque de tiempo por ID."""
        time_block = self.repository.get(time_block_id)
        if not time_block:
            raise HTTPException(
                status_code=404, detail=f"TimeBlock with ID {time_block_id} not found"
            )
        return time_block

    def create_time_block(self, time_block_data: CreateTimeBlockRequest):
        """Crea un nuevo bloque de tiempo."""
        return self.repository.create(time_block_data.model_dump())

    def create_hours(self):
        """Crea todas las horas y las inserta si no estan en la BD"""

        all_hours = [
            {"name": "Hora 1", "start": "07:50", "end": "08:40"},
            {"name": "Hora 2", "start": "08:45", "end": "09:35"},
            {"name": "Hora 3", "start": "09:35", "end": "10:25"},
            {"name": "Hora 4", "start": "10:30", "end": "11:20"},
            {"name": "Hora 5", "start": "11:20", "end": "12:10"},
            {"name": "Hora 6", "start": "12:15", "end": "13:10"},
            {"name": "Hora 7", "start": "13:10", "end": "14:00"},
            {"name": "Hora 8", "start": "14:00", "end": "14:50"},
            {"name": "Hora 9", "start": "14:55", "end": "15:45"},
        ]

        for hour in all_hours:
            existing_hour = self.hours_repository.get_all()
            if not any(
                h.start == hour["start"] and h.end == hour["end"] for h in existing_hour
            ):
                self.hours_repository.create(hour)

    def create_all_time_block(
        self,
        num_time_block: Integer,
        start_num_time_block: Integer,
        day: Integer,
        week_id: Integer,
    ):
        """
        Crea todos los bloques de tiempo segun ciertos parametros

        @param num_time_block[Integer]: Numero de bloques de tiempo a insertar
        @param start_num_time_block[Integer]: Numero de bloque de tiempo que comenzara
        @day[Integer]: El dia que le pertenece al bloque de tiempo
        @week_id[Integer]: El id de la semana que le corresponde al bloque de tiempo
        """

        if start_num_time_block < 1 or start_num_time_block > len(hours):
            raise HTTPException(
                status_code=404,
                detail=f"start_num_time_block with ID {start_num_time_block} not found",
            )

        if day < 1 or day > 7:
            raise HTTPException(status_code=404, detail="day with ID {day} not found")

        weeks = self.week_repository.get(week_id)
        if not weeks:
            raise HTTPException(
                status_code=404, detail=f"Weeks with ID {week_id} not found"
            )

        self.create_hours()
        hours = self.hours_repository.get_all()

        # Filtrar las horas a partir de la hora_inicio
        hours_filter = [hora for hora in hours if hora.id >= start_num_time_block]

        if len(hours_filter) < num_time_block:
            raise HTTPException(
                status_code=404,
                detail=f"Weeks with ID {num_time_block} not found",
            )

        # Crear n bloques de tiempo comenzando desde hora_inicio
        for i in range(num_time_block):
            # Seleccionar las horas desde hora_inicio
            existing_hour = hours_filter[i]

            existing_block = self.repository.get_all()
            if not any(
                time_block.semana_id == week_id
                and time_block.day == day
                and time_block.hour_id == existing_hour.id
                for time_block in existing_block
            ):
                self.repository.create(
                    {
                        "semana_id": week_id,
                        "dia": day,
                        "hora_id": existing_hour.id,
                        "created_at": datetime.utcnow(),
                        "updated_at": datetime.utcnow(),
                    }
                )

    def update_time_block(
        self, time_block_id: int, time_block_data: CreateTimeBlockRequest
    ):
        """Actualiza un bloque de tiempo existente."""
        time_block = self.repository.get(time_block_id)
        if not time_block:
            raise HTTPException(
                status_code=404, detail=f"TimeBlock with ID {time_block_id} not found"
            )
        return self.repository.update(time_block, time_block_data.model_dump())

    def delete_time_block(self, time_block_id: int):
        """Elimina un bloque de tiempo por ID."""
        time_block = self.repository.get(time_block_id)
        if not time_block:
            raise HTTPException(
                status_code=404, detail=f"TimeBlock with ID {time_block_id} not found"
            )
        return self.repository.delete(time_block_id)
