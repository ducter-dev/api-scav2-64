from openopc2.da_client import OpcDaClient
import pywintypes
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

pywintypes.datetime = pywintypes.TimeType

SERVER_OPC = os.environ.get('OPC_SERVER')
HOST_OPC = os.environ.get('OPC_HOST')
sync = False

class OpcServices():
    server = SERVER_OPC
    host = HOST_OPC
    opc = OpcDaClient()
    activo = False
    
    @classmethod
    def conectarOPC(self):
        try:
            print(self.opc)
            self.opc.connect(self.server, self.host)
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