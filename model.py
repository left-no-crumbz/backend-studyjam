from datetime import datetime, timezone

import sqlalchemy as sa
import sqlalchemy.orm as so

from extensions import db

# NOTE: since we didn't implement any migrations,
# always remember to delete and let the app create
# a new db when you change something from this file.
# The notion page I provided delves into migration if
# you're interested ^_^


class QuestionModel(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    question: so.Mapped[str] = so.mapped_column(sa.String(256))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self) -> str:
        return f"User {self.username}"
