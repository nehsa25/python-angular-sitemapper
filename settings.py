from dataclasses import dataclass, field
import enum


@dataclass
class PriorityOverride:
    page: str
    priority: int
  
@dataclass
class Mapping:
    folder: str
    url_path: str
      
@dataclass # Dataclass to store settings
class Settings:     
    base_url: str = "" 
    use_hash: bool = True
    mappings: list[Mapping] = field(default_factory=list)
    priority_overrides: list[PriorityOverride] = field(default_factory=list)
    ignore_folders: list[str] = field(default_factory=list)
    
