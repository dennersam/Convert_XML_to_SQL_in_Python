import xmltodict
import json

def retornaDicionario(xml):
    return json.dumps(xmltodict.parse(xml), indent=2)

if __name__=='__main__':
    with open('dados/77_POSTO_VIP.xml.xml', 'r') as f:
        data = f.read()
        dicionario = retornaDicionario(data)

dados = json.loads(dicionario)

cnpj = dados['nfeProc']['NFe']['infNFe']['emit']['CNPJ']
ch = dados['nfeProc']['NFe']['infNFe']["@Id"]
chave = ch[3:]
nome = dados['nfeProc']['NFe']['infNFe']['emit']['xNome']
n_fantasia = dados['nfeProc']['NFe']['infNFe']['emit']['xFant']
logadouro = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xLgr']
numero = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['nro']
bairro = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xBairro']
cMunicipio = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['cMun']
municipio = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xMun']
uf = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['UF']
cep = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['CEP']
cPais = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['cPais']
xPais = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xPais']
fone = dados['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['fone']
iestadual = dados['nfeProc']['NFe']['infNFe']['emit']['IE']

arquivo = open("C:\Diretorio\export.sql", "a")

content = list()
content.append(nome)
content.append(n_fantasia)
content.append(cnpj)
content.append(chave)
content.append(logadouro)
content.append(numero)
content.append(bairro)
content.append(municipio)
content.append(cMunicipio)
content.append(uf)
content.append(cep)
content.append(cPais)
content.append(fone)
content.append(iestadual)

sql = "INSERT INTO dbo.FCFO VALUES (1,0001," + n_fantasia + "," + nome + ",null," + iestadual + ",null," + logadouro + "," + numero + ",null," + bairro + "," + municipio + "," + uf + "," + cep + "," + fone + "," + logadouro + "," + numero + ",null," + bairro + "," + municipio + "," + uf + "," + cep + "," + fone + "," + logadouro + "," + numero + ",null," + bairro + "," + logadouro + "," + uf + "," + cep + "," + fone + ",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null," + cMunicipio + ",null,null,null,null,null,null,null,null," + xPais + "," + xPais + "," + xPais + ",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null," + cMunicipio + "," + cMunicipio + ",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null)"

arquivo.writelines(sql)