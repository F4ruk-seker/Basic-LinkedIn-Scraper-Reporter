from dataclasses import dataclass


@dataclass
class PersonSearchModel:
    name: str | None
    title: str | None
    country: str | None
    details: list[str] | None

    @classmethod
    def load_default(cls):
        return cls(None, None, None, None)

