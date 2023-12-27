from openopc2.utils import get_opc_da_client
from openopc2.config import OpenOpcConfig
import time
#import pywintypes
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#pywintypes.datetime = pywintypes.TimeType
OpenOpcConfig.OPC_SERVER =  os.environ.get('OPC_SERVER')
OpenOpcConfig.OPC_GATEWAY_HOST =  os.environ.get('OPC_GATE_HOST')
OpenOpcConfig.OPC_GATEWAY_PORT =  os.environ.get('OPC_GATE_PORT')
OpenOpcConfig.OPC_MODE =  os.environ.get('OPC_MODE')
OpenOpcConfig.OPC_CLASS =  os.environ.get('OPC_CLASS')
OpenOpcConfig.OPC_HOST =  os.environ.get('OPC_HOST')

config = OpenOpcConfig
opc_client = get_opc_da_client(config)
sync = False

class OpcServices():
    server = config.OPC_SERVER
    host = config.OPC_GATEWAY_HOST
    opc = opc_client
    activo = False
    
    @classmethod
    def conectarOPC(self):
        try:
            print(self.opc)
            #self.opc.connect(self.server, self.host)
            self.activo = True
            print(f'servidor opc: {self.activo}')
            return True
        except Exception as e:
            self.activo = False
            print(f'Error: {e}')
            return False

    @classmethod
    def readDataPLC(self, tag):
        try:
            print(f'tag: {tag}')
            value = self.opc.read(tag, sync=sync)
            print(f'value: {value}')
            return value[0]
        except Exception as e:
            print(f'Error: {e}')
            return False
    
    @classmethod
    def writeOPC(self, tag, value):
        try:
            self.opc.write((tag, value))
            return value
        except Exception as e:
            print(f'Error: {e}')
            return False