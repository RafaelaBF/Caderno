# Pesquisa formatar o pc sozinho
Pesquisa de como fazer um pendrive ou script que o pc sozinho

<!-- TOC -->
* [Pesquisa formatar o pc sozinho](#pesquisa-formatar-o-pc-sozinho)
  * [🤖 Resposta do chatGPT](#-resposta-do-chatgpt)
    * [Formatação de Drive (Windows):](#formatação-de-drive-windows)
    * [Instalação do Sistema Operacional:](#instalação-do-sistema-operacional)
    * [Formatação de Disco (Linux):](#formatação-de-disco-linux)
  * [Fontes](#fontes)
<!-- TOC -->

## 🤖 Resposta do chatGPT
Para criar um script de formatação de um computador (PC), é importante entender qual tipo de formatação você está procurando. Aqui estão alguns exemplos de scripts de formatação para diferentes propósitos:

### Formatação de Drive (Windows):

Este script pode ser usado para formatar um drive específico no Windows usando o utilitário `format`:

```batsh
    @echo off
    echo Formatando o Drive C:...
    format C: /FS:NTFS /Q /V:SISTEMA
```
* Salve o código acima em um arquivo de lote **(.bat)** e execute como administrador.

### Instalação do Sistema Operacional:

* Se você deseja formatar e instalar um sistema operacional, você pode automatizar o processo usando ferramentas como o `AutoUnattend.xml` no caso do Windows.

Exemplo para criar um script de instalação não assistida do Windows:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="oobeSystem">
        <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <OOBE>
                <HideEULAPage>true</HideEULAPage>
                <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
            </OOBE>
        </component>
    </settings>
</unattend>
```
### Formatação de Disco (Linux):
* Para formatar um disco no Linux, você pode usar o comando `mkfs`:

```bash
    #!/bin/bash
    echo "Formatando o disco /dev/sdX..."
    mkfs.ext4 /dev/sdX
```
* Lembre-se de substituir `/dev/sdX` pelo caminho real do seu dispositivo.

Estes são exemplos básicos e genéricos. Dependendo do seu cenário específico, os scripts podem precisar de ajustes adicionais. Certifique-se de entender completamente o impacto de qualquer script de formatação antes de executá-lo, especialmente se envolver dados importantes.

## Fontes
* [ChatGpt](https://chat.openai.com/)
