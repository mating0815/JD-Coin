

from .bean import Bean
from .bean_app import BeanApp
from .bean_jr import SignJR
from .daka_app import DakaApp
from .data_station import DataStation
from .double_jr import DoubleSign_JR
from .jdstock_sign import JDStock_Sign

__all__ = ['jobs_all']

jobs_all = [Bean, SignJR, DakaApp, BeanApp, DataStation, JDStock_Sign]
