# TESTE DA API

## Menu

- [Caso de Testes](#caso-de-testes)
- [Iniciar Teste Automatizado](#iniciar-teste-automatizado)

Para criar casos de teste para essa aplicação, podemos considerar os seguintes cenários:


## Caso de Testes

### Caso1: Valid JWT With Correct Claims
- Justificativa: Abrindo o JWT com as informações do Name sem números, Role como "Admin", e Seed sendo um número primo.

- Entrada:
`eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05sIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg`
    ```json
    {
        "Role": "Admin",
        "Seed": "7841",
        "Name": "Toninho Araujo"
    }
    ```
 - Saida: ***`verdadeiro`***
  

### Caso2: Invalid JWT Missing Claim
- Justificativa: Abrindo o JWT sem uma das claims necessárias Name, Role ou Seed.

- Entrada:
`eyJhbGciOiJIUzI1NiJ9.eyJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.GeH_kHSsRrmTY2MQI0v_NccrkBBLxwX6NJA1P2nKEeA`
    ```json
    {
        "Seed": "7841", 
        "Name": "Toninho Araujo"
    }
    ```
- Saida: ***`falso`***

 
### Caso3: Invalid JWT With Extra Claim
- Justificativa: Abrindo o JWT com uma claim extra que não seja Name, Role ou Seed.

- Entrada:
`eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiTWVtYmVyIiwiT3JnIjoiQlIiLCJTZWVkIjoiMTQ2MjciLCJOYW1lIjoiVmFsZGlyIEFyYW5oYSJ9.cmrXV_Flm5mfdpfNUVopY_I2zeJUy4EZ4i3Fea98zvY`    
    ```json
    {
        "Role": "Member",
        "Org": "BR",
        "Seed": "14627",
        "Name": "Valdir Aranha"
    }
    ```
- Saida: ***`falso`***


### Caso4: Invalid JWT With Numeric Name
- Justificativa: Abrindo o JWT onde a claim Name contém números.

- Entrada:
`eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiRXh0ZXJuYWwiLCJTZWVkIjoiODgwMzciLCJOYW1lIjoiTTRyaWEgT2xpdmlhIn0.6YD73XWZYQSSMDf6H0i3-kylz1-TY_Yt6h1cV2Ku-Qs`
    ```json
    {
        "Role": "External",
        "Seed": "88037",
        "Name": "M4ria Olivia"
    }
    ```
- Saida: ***`falso`***


### Caso5: Invalid JWT With Long Name
- Justificativa: Abrindo o JWT onde a claim Name excede 256 caracteres.

- Entrada:
`eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiTWVtYmVyIiwiU2VlZCI6IjE0NjI3IiwiTmFtZSI6Ik1hcmNvcyBSdWl6IGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEifQ.zClX-uOKKqLsqAqVMpnw-I0EnMe10udOMtITFc0EHUk`
    ```json
    {
        "Role": "Member",
        "Seed": "14627",
        "Name": "Marcos Ruiz aaaaaaaaaa aaaaaaaaaa aaaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa"
    }
    ```
- Saida: ***`falso`***


### Caso6: Invalid JWT With Non-Prime Seed
- Justificativa: Abrindo o JWT onde a claim Seed não é um número primo.

- Entrada:
`eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiMTQ2MjYiLCJOYW1lIjoiTWFyY29zIFJ1aXoifQ.DEmgzTbgiW0sL1BAf2gKQTRnPtnuIZHIBq1Ejzllk7w`
    ```json
    {
        "Role": "Admin",
        "Seed": "14626",
        "Name": "Marcos Ruiz"
    }
    ```
- Saida: ***`falso`***


### Caso7: Invalid JWT With Invalid Role
- Justificativa: Abrindo o JWT

- Entrada:
`eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW5pc3RyYWRvciIsIlNlZWQiOiI3ODQxIiwiTmFtZSI6Ik1hcmNvcyBSdWl6In0.PPc15UX8ndSPsVk3HqqK3la6GYQhfDTyadUXPodfDrc`
    ```json
    {
        "Role": "Administrador",
        "Seed": "7841",
        "Name": "Marcos Ruiz"
    }
    ```
- Saida: ***`falso`***


> [!NOTE] 
> Esses casos de teste cobrem as principais condições da aplicação.


## Iniciar Teste Automatizado
> [!IMPORTANT]
>**Verify Jwt** é uma função hipotética simulando a chamada desta API. 

### Passo 1: Criar um Ambiente Virtual
Navegue até o diretório do seu projeto:
```bash
cd jwt_robot
```
Crie um ambiente virtual chamado venv:
```bash
python -m venv venv
```
### Passo 2: Ativar o Ambiente Virtual
Ative o ambiente virtual. O comando varia de acordo com o sistema operacional.

No Windows:
```bash
venv\Scripts\activate
```
No macOS/Linux:
```bash
source venv/bin/activate
```
### Passo 3: Instalar as Dependências
Instale as dependências usando o pip:
```bash
pip install -r requirements.txt
```

### Passo 4: Execução dos testes
```bash
robot -d results tests
```

### Passo 5: Resultado dos testes

Abrir no navegador de sua preferencia o resultado dos teste gravados no arquivo `results/report.html`