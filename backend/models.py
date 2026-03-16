from sqlalchemy import Column, Integer, Float, String
from database import Base

class CancerRate(Base):
    __tablename__ = "cancer_rates"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    sex = Column(String)
    type = Column(String)
    cancer_type = Column(String)
    age_std_rate_aust = Column(Float)
    age_std_rate_segi = Column(Float)
    age_std_rate_who = Column(Float)

class CancerRatio(Base):
    __tablename__ = "cancer_ratios"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    sex = Column(String)
    cancer_type = Column(String)
    aust_ratio = Column(Float)
    segi_ratio = Column(Float)
    who_ratio = Column(Float)

class UVSummary(Base):
    __tablename__ = "uv_summary"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    generation = Column(String)
    date = Column(String)
    max_uv_index = Column(Float)
    avg_temperature = Column(Float)