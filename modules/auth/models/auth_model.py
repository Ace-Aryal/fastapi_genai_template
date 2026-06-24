from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from infrastructures.database.base import Base


class UserRole:
    ADMIN = "admin"
    USER = "user"


class AuthModel(Base):
    __tablename__ = "auth"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[str] = mapped_column(String(50), default=UserRole.USER, nullable=False)
    # Relationships
    profile_id: Mapped[int] = mapped_column(Integer, ForeignKey("profile.id"))
    profile: Mapped["ProfileModel"] = relationship(
        "ProfileModel", back_populates="auth", uselist=False
    )


class ProfileModel(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    bio: Mapped[str] = mapped_column(String(255), nullable=True)

    # Relationships
    auth: Mapped["AuthModel"] = relationship(
        "AuthModel", back_populates="profile", uselist=False
    )
