import uuid
from sqlalchemy import Column, String, Float, Date, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.db import Base
import enum

# Define an Enum class using Python's enum module
class ActivityStatus(enum.Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    
class Foreman(Base):
    __tablename__ = "foreman"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=True)

    activities = relationship("Activity", back_populates="foreman")

class Activity(Base):
    __tablename__ = "activity"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)

    duration = Column(Float, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    status = Column(String(50), Enum(ActivityStatus), default=ActivityStatus.PENDING)

    foreman_id = Column(UUID(as_uuid=True), ForeignKey("foreman.id"), nullable=True)

    foreman = relationship("Foreman", back_populates="activities")
    material_assignments = relationship("MaterialAssignment", back_populates="activity")


class Material(Base):
    __tablename__ = "material"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    unit = Column(String(50), nullable=False)
    cost_per_unit = Column(Float, nullable=False)

    inventories = relationship("Inventory", back_populates="material")
    material_assignments = relationship("MaterialAssignment", back_populates="material")


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    material_id = Column(UUID(as_uuid=True), ForeignKey("material.id"), nullable=False)
    quantity_in_stock = Column(Float, nullable=False)
    threshold = Column(Float, nullable=False)

    material = relationship("Material", back_populates="inventories")


class MaterialAssignment(Base):
    __tablename__ = "material_assignment"

    assignment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    activity_id = Column(UUID(as_uuid=True), ForeignKey("activity.id"), nullable=False)
    material_id = Column(UUID(as_uuid=True), ForeignKey("material.id"), nullable=False)
    quantity_assigned = Column(Float, nullable=False)
    date_assigned = Column(Date, nullable=False)

    activity = relationship("Activity", back_populates="material_assignments")
    material = relationship("Material", back_populates="material_assignments")
