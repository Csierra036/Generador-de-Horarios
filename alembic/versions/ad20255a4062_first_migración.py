"""First migración

Revision ID: ad20255a4062
Revises: 
Create Date: 2025-01-31 09:26:31.910060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad20255a4062'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('academic_period',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('actual', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_academic_period_actual'), 'academic_period', ['actual'], unique=False)
    op.create_index(op.f('ix_academic_period_id'), 'academic_period', ['id'], unique=False)
    op.create_index(op.f('ix_academic_period_name'), 'academic_period', ['name'], unique=False)
    op.create_index(op.f('ix_academic_period_number'), 'academic_period', ['number'], unique=False)
    op.create_index(op.f('ix_academic_period_year'), 'academic_period', ['year'], unique=False)
    op.create_table('campus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_campus_id'), 'campus', ['id'], unique=False)
    op.create_index(op.f('ix_campus_location'), 'campus', ['location'], unique=False)
    op.create_index(op.f('ix_campus_name'), 'campus', ['name'], unique=False)
    op.create_table('careers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_careers_fullname'), 'careers', ['fullname'], unique=False)
    op.create_index(op.f('ix_careers_id'), 'careers', ['id'], unique=False)
    op.create_table('classrooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('capacidad', sa.Integer(), nullable=True),
    sa.Column('ubicacion', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classrooms_capacidad'), 'classrooms', ['capacidad'], unique=False)
    op.create_index(op.f('ix_classrooms_id'), 'classrooms', ['id'], unique=False)
    op.create_index(op.f('ix_classrooms_nombre'), 'classrooms', ['nombre'], unique=False)
    op.create_index(op.f('ix_classrooms_ubicacion'), 'classrooms', ['ubicacion'], unique=False)
    op.create_table('hours',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('start', sa.String(), nullable=True),
    sa.Column('end', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hours_end'), 'hours', ['end'], unique=False)
    op.create_index(op.f('ix_hours_id'), 'hours', ['id'], unique=False)
    op.create_index(op.f('ix_hours_name'), 'hours', ['name'], unique=False)
    op.create_index(op.f('ix_hours_start'), 'hours', ['start'], unique=False)
    op.create_table('modality',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_modality_id'), 'modality', ['id'], unique=False)
    op.create_index(op.f('ix_modality_name'), 'modality', ['name'], unique=True)
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teachers_first_name'), 'teachers', ['first_name'], unique=False)
    op.create_index(op.f('ix_teachers_id'), 'teachers', ['id'], unique=False)
    op.create_index(op.f('ix_teachers_last_name'), 'teachers', ['last_name'], unique=False)
    op.create_table('career_campus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('career_id', sa.Integer(), nullable=True),
    sa.Column('campus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['campus_id'], ['campus.id'], ),
    sa.ForeignKeyConstraint(['career_id'], ['careers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_career_campus_campus_id'), 'career_campus', ['campus_id'], unique=False)
    op.create_index(op.f('ix_career_campus_career_id'), 'career_campus', ['career_id'], unique=False)
    op.create_index(op.f('ix_career_campus_id'), 'career_campus', ['id'], unique=False)
    op.create_table('career_period',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('career_id', sa.Integer(), nullable=True),
    sa.Column('period_id', sa.Integer(), nullable=True),
    sa.Column('schedule_generated', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['career_id'], ['careers.id'], ),
    sa.ForeignKeyConstraint(['period_id'], ['academic_period.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_career_period_career_id'), 'career_period', ['career_id'], unique=False)
    op.create_index(op.f('ix_career_period_id'), 'career_period', ['id'], unique=False)
    op.create_index(op.f('ix_career_period_period_id'), 'career_period', ['period_id'], unique=False)
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('career_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('at_laboratory', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['career_id'], ['careers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_courses_active'), 'courses', ['active'], unique=False)
    op.create_index(op.f('ix_courses_at_laboratory'), 'courses', ['at_laboratory'], unique=False)
    op.create_index(op.f('ix_courses_career_id'), 'courses', ['career_id'], unique=False)
    op.create_index(op.f('ix_courses_id'), 'courses', ['id'], unique=False)
    op.create_index(op.f('ix_courses_name'), 'courses', ['name'], unique=False)
    op.create_table('weeks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('period_id', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['period_id'], ['academic_period.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weeks_id'), 'weeks', ['id'], unique=False)
    op.create_index(op.f('ix_weeks_number'), 'weeks', ['number'], unique=False)
    op.create_index(op.f('ix_weeks_period_id'), 'weeks', ['period_id'], unique=False)
    op.create_table('sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('modality_id', sa.Integer(), nullable=True),
    sa.Column('academic_period_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['academic_period_id'], ['academic_period.id'], ),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['modality_id'], ['modality.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sections_academic_period_id'), 'sections', ['academic_period_id'], unique=False)
    op.create_index(op.f('ix_sections_course_id'), 'sections', ['course_id'], unique=False)
    op.create_index(op.f('ix_sections_id'), 'sections', ['id'], unique=False)
    op.create_index(op.f('ix_sections_modality_id'), 'sections', ['modality_id'], unique=False)
    op.create_index(op.f('ix_sections_name'), 'sections', ['name'], unique=False)
    op.create_table('time_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hour_id', sa.Integer(), nullable=True),
    sa.Column('week_id', sa.Integer(), nullable=True),
    sa.Column('day', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hour_id'], ['hours.id'], ),
    sa.ForeignKeyConstraint(['week_id'], ['weeks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_time_blocks_day'), 'time_blocks', ['day'], unique=False)
    op.create_index(op.f('ix_time_blocks_hour_id'), 'time_blocks', ['hour_id'], unique=False)
    op.create_index(op.f('ix_time_blocks_id'), 'time_blocks', ['id'], unique=False)
    op.create_index(op.f('ix_time_blocks_week_id'), 'time_blocks', ['week_id'], unique=False)
    op.create_table('room_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['time_blocks.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['classrooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_blocks_block_id'), 'room_blocks', ['block_id'], unique=False)
    op.create_index(op.f('ix_room_blocks_id'), 'room_blocks', ['id'], unique=False)
    op.create_index(op.f('ix_room_blocks_room_id'), 'room_blocks', ['room_id'], unique=False)
    op.create_table('section_teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('section_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('assigned_hours', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['section_id'], ['sections.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_section_teacher_assigned_hours'), 'section_teacher', ['assigned_hours'], unique=False)
    op.create_index(op.f('ix_section_teacher_id'), 'section_teacher', ['id'], unique=False)
    op.create_index(op.f('ix_section_teacher_section_id'), 'section_teacher', ['section_id'], unique=False)
    op.create_index(op.f('ix_section_teacher_teacher_id'), 'section_teacher', ['teacher_id'], unique=False)
    op.create_table('section_weeks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('section_id', sa.Integer(), nullable=True),
    sa.Column('week_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['section_id'], ['sections.id'], ),
    sa.ForeignKeyConstraint(['week_id'], ['weeks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_section_weeks_id'), 'section_weeks', ['id'], unique=False)
    op.create_index(op.f('ix_section_weeks_section_id'), 'section_weeks', ['section_id'], unique=False)
    op.create_index(op.f('ix_section_weeks_week_id'), 'section_weeks', ['week_id'], unique=False)
    op.create_table('teacher_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('time_block_id', sa.Integer(), nullable=True),
    sa.Column('academic_period_id', sa.Integer(), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['academic_period_id'], ['academic_period.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.ForeignKeyConstraint(['time_block_id'], ['time_blocks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teacher_time_academic_period_id'), 'teacher_time', ['academic_period_id'], unique=False)
    op.create_index(op.f('ix_teacher_time_id'), 'teacher_time', ['id'], unique=False)
    op.create_index(op.f('ix_teacher_time_teacher_id'), 'teacher_time', ['teacher_id'], unique=False)
    op.create_index(op.f('ix_teacher_time_time_block_id'), 'teacher_time', ['time_block_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_teacher_time_time_block_id'), table_name='teacher_time')
    op.drop_index(op.f('ix_teacher_time_teacher_id'), table_name='teacher_time')
    op.drop_index(op.f('ix_teacher_time_id'), table_name='teacher_time')
    op.drop_index(op.f('ix_teacher_time_academic_period_id'), table_name='teacher_time')
    op.drop_table('teacher_time')
    op.drop_index(op.f('ix_section_weeks_week_id'), table_name='section_weeks')
    op.drop_index(op.f('ix_section_weeks_section_id'), table_name='section_weeks')
    op.drop_index(op.f('ix_section_weeks_id'), table_name='section_weeks')
    op.drop_table('section_weeks')
    op.drop_index(op.f('ix_section_teacher_teacher_id'), table_name='section_teacher')
    op.drop_index(op.f('ix_section_teacher_section_id'), table_name='section_teacher')
    op.drop_index(op.f('ix_section_teacher_id'), table_name='section_teacher')
    op.drop_index(op.f('ix_section_teacher_assigned_hours'), table_name='section_teacher')
    op.drop_table('section_teacher')
    op.drop_index(op.f('ix_room_blocks_room_id'), table_name='room_blocks')
    op.drop_index(op.f('ix_room_blocks_id'), table_name='room_blocks')
    op.drop_index(op.f('ix_room_blocks_block_id'), table_name='room_blocks')
    op.drop_table('room_blocks')
    op.drop_index(op.f('ix_time_blocks_week_id'), table_name='time_blocks')
    op.drop_index(op.f('ix_time_blocks_id'), table_name='time_blocks')
    op.drop_index(op.f('ix_time_blocks_hour_id'), table_name='time_blocks')
    op.drop_index(op.f('ix_time_blocks_day'), table_name='time_blocks')
    op.drop_table('time_blocks')
    op.drop_index(op.f('ix_sections_name'), table_name='sections')
    op.drop_index(op.f('ix_sections_modality_id'), table_name='sections')
    op.drop_index(op.f('ix_sections_id'), table_name='sections')
    op.drop_index(op.f('ix_sections_course_id'), table_name='sections')
    op.drop_index(op.f('ix_sections_academic_period_id'), table_name='sections')
    op.drop_table('sections')
    op.drop_index(op.f('ix_weeks_period_id'), table_name='weeks')
    op.drop_index(op.f('ix_weeks_number'), table_name='weeks')
    op.drop_index(op.f('ix_weeks_id'), table_name='weeks')
    op.drop_table('weeks')
    op.drop_index(op.f('ix_courses_name'), table_name='courses')
    op.drop_index(op.f('ix_courses_id'), table_name='courses')
    op.drop_index(op.f('ix_courses_career_id'), table_name='courses')
    op.drop_index(op.f('ix_courses_at_laboratory'), table_name='courses')
    op.drop_index(op.f('ix_courses_active'), table_name='courses')
    op.drop_table('courses')
    op.drop_index(op.f('ix_career_period_period_id'), table_name='career_period')
    op.drop_index(op.f('ix_career_period_id'), table_name='career_period')
    op.drop_index(op.f('ix_career_period_career_id'), table_name='career_period')
    op.drop_table('career_period')
    op.drop_index(op.f('ix_career_campus_id'), table_name='career_campus')
    op.drop_index(op.f('ix_career_campus_career_id'), table_name='career_campus')
    op.drop_index(op.f('ix_career_campus_campus_id'), table_name='career_campus')
    op.drop_table('career_campus')
    op.drop_index(op.f('ix_teachers_last_name'), table_name='teachers')
    op.drop_index(op.f('ix_teachers_id'), table_name='teachers')
    op.drop_index(op.f('ix_teachers_first_name'), table_name='teachers')
    op.drop_table('teachers')
    op.drop_index(op.f('ix_modality_name'), table_name='modality')
    op.drop_index(op.f('ix_modality_id'), table_name='modality')
    op.drop_table('modality')
    op.drop_index(op.f('ix_hours_start'), table_name='hours')
    op.drop_index(op.f('ix_hours_name'), table_name='hours')
    op.drop_index(op.f('ix_hours_id'), table_name='hours')
    op.drop_index(op.f('ix_hours_end'), table_name='hours')
    op.drop_table('hours')
    op.drop_index(op.f('ix_classrooms_ubicacion'), table_name='classrooms')
    op.drop_index(op.f('ix_classrooms_nombre'), table_name='classrooms')
    op.drop_index(op.f('ix_classrooms_id'), table_name='classrooms')
    op.drop_index(op.f('ix_classrooms_capacidad'), table_name='classrooms')
    op.drop_table('classrooms')
    op.drop_index(op.f('ix_careers_id'), table_name='careers')
    op.drop_index(op.f('ix_careers_fullname'), table_name='careers')
    op.drop_table('careers')
    op.drop_index(op.f('ix_campus_name'), table_name='campus')
    op.drop_index(op.f('ix_campus_location'), table_name='campus')
    op.drop_index(op.f('ix_campus_id'), table_name='campus')
    op.drop_table('campus')
    op.drop_index(op.f('ix_academic_period_year'), table_name='academic_period')
    op.drop_index(op.f('ix_academic_period_number'), table_name='academic_period')
    op.drop_index(op.f('ix_academic_period_name'), table_name='academic_period')
    op.drop_index(op.f('ix_academic_period_id'), table_name='academic_period')
    op.drop_index(op.f('ix_academic_period_actual'), table_name='academic_period')
    op.drop_table('academic_period')
    # ### end Alembic commands ###
