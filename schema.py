import graphene
from graphene import List, Argument, Int
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import text

from database import db_session, engine
from models.city_model import CityModel
from models.target_model import TargetModel
from models.country_model import CountryModel
from models.mission_model import MissionModel
from models.targettype_model import TargetTypeModel

class City(SQLAlchemyObjectType):
    class Meta:
        model = CityModel
        interfaces = (graphene.relay.Node,)

class Target(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (graphene.relay.Node,)

class Country(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (graphene.relay.Node,)

class Mission(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (graphene.relay.Node,)

class TargetType(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypeModel
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    mission_by_id = graphene.Field(Mission, mission_id=graphene.Int(required=True))
    missions_by_range_date = graphene.List(Mission,
                                           start_date=graphene.Date(required=True),
                                           end_date=graphene.Date( required=True))


    def resolve_mission_by_id(self, info, mission_id):
        return db_session.query(MissionModel).get(mission_id)

    def resolve_missions_by_range_date(self, info, start_date, end_date):
        return db_session.query(MissionModel).filter(MissionModel.mission_date.between(start_date,end_date)).all()


schema = graphene.Schema(query=Query)