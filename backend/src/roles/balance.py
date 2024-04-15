from fastapi import Depends, Request
from database.conn import conn
from fastapi import HTTPException
from oracledb import DatabaseError
from fastapi import HTTPException
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from fastapi import Request
from typing import List


#Calcula o preço de venda com base nos custos, comissões, impostos e margem de lucro desejada.
#Retorna o preço de venda calculado.

def calcular_preco_venda(custo_produto:float, custo_fixo_pct:float, comissao_venda_pct:float, imposto_venda_pct:float, margem_lucro_pct:float):
    if not 0 <= custo_fixo_pct <= 100 or not 0 <= comissao_venda_pct <= 100 or \
 not 0 <= imposto_venda_pct <= 100 or not 0 <= margem_lucro_pct <= 100:
        raise ValueError("Percentuais devem estar entre 0 e 100.")

    fatores = (custo_fixo_pct + comissao_venda_pct + imposto_venda_pct + margem_lucro_pct) / 100
    if fatores >= 1:
        raise ValueError("A soma dos percentuais não pode ser igual ou maior que 100%.")

    return custo_produto / (1 - fatores)
