import discord
import random
import requests
import json
import base
import time
import os
import strings
import asciiBot
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.utils import get

VERMELHO = 0xff0000

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '$', intents = intents)


def _save(amounts):
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

def _casaisSave(casais):
    with open('casais.json', 'w+') as c:
        json.dump(casais, c)

global amounts
def ler_amounts():
    with open('amounts.json') as f:
        amounts = json.loads(f.read())
        return amounts


def _save_ddiamonds(ddiamonds):
    with open('ddiamond.json', 'w+') as d:
        json.dump(ddiamonds, d) 


def preco_ddiamond():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/USD')

    cotacao = json.loads(requisicao.text)
    ddiamond = cotacao['USD'] ['bid']
    ddiamond = float(ddiamond) * 100.0
    return ddiamond 


global casais
with open('casais.json') as c:
    casais = json.loads(c.read())

global preco
preco = int(preco_ddiamond())

@client.event
async def on_guild_join(guild):
     for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Oiie lindosss e lindasss')
            await channel.send('Me da permissao maxima ai p eu conseguir te ajudar :/')
        break

@client.event
async def on_ready():
    print("Bot ta online!")

    list_guilds = client.guilds
    servers = len(list_guilds)

    atividade = f"$help | Estou em {servers} servidores!"

    activity = discord.Activity(name=atividade, type=discord.ActivityType.watching) #status assistindo
    #await client.change_presence(game=discord.Game(name="on " + str(len(client.servers)) + " Servers.", type=0))
    await client.change_presence(activity=activity)

    #print(dir())

    global amounts
    with open('amounts.json') as f:
        amounts = json.loads(f.read())


   # global casais_lidos
   # casais_lidos = json.loads('casais.json')



    global descricao_opc_dog
    descricao_opc_dog= ['Woof!', 'Auau!']

    global descricao_opc_cat
    descricao_opc_cat = ['Nya*', 'Meow']


    global embed_help
    embed_help = discord.Embed(title = "Meus comandos:", color = VERMELHO, description="""
$animais
$donate
$cotacao
$administracao
$interacao
$comopegarid
$creditos
$infccoins
$atts - ultimas atts do bot
$previsaoatts""")


    global embed_casamento1
    embed_casamento1 = discord.Embed(title="Casamento", color = VERMELHO, description = f"""
Para completar o casamento, a pessoa marcada tem que reagir com '❤️' nessa mensagem. Para rejeitar, e so reagir com '💔'.
pedido de casamento ira expirar em 30 segundos.""")


    global embed_divorcio
    embed_divorcio = discord.Embed(title="Divorcio", color = VERMELHO, description=f"Tem certeza que voce quer pedir divorcio? Awnn, voces eram perfeitos juntos! Se quiser mesmo, e so reajir com '👋' aqui... :cry:")

    global embed_ccoins
    embed_ccoins = discord.Embed(title = "Ccoins", color = VERMELHO, description = """
(PENSANDO AINDA EM POSSIVEIS UPGRADES, RELEVEM)
=> Comandos:
$ccoins - Ver a quantidade de coins que vc tem
$transferir <QUANTIDADE> @
$registrar - cria uma conta no ccoins central bank! \n
=> Como conseguir ccoins:
- 
-
-\n
=> O que fazer com ccoins
-
-
-
-
-\n
=> Ideias:
-> Investir ccoins baseadas em acoes reais
-> Comprar coisas (ainda n sei oq)
-> Apostar""")

    global embed_att
    embed_att = discord.Embed(title = "Ultimas atualizacoes do bot", color = VERMELHO, description = r"""
1. Agora para interagir com alguem, e preciso marca-la, nao usar o id
2. Correcoes de bugs
3. Nova aba de atts do bot
4. Nova aba de atts futuras
5. Ban, e kick por marcacao (@)
6. Easter eggs!
7. Maior variedade de fotos de animais
8. Nova aba de membros banidos
""")

    global embed_atts_prievistas
    embed_atts_prievistas = discord.Embed(title = "Atualizacoes previstas", color = VERMELHO, description = r"""
1. Adicionar mais gifs e fotos em todos os topicos para aumentar a variedade
2. Criar mais interacoes
3. Adicionar mais funcoes de administramento
4. Adicionar mais animais a lista
5. Corrigir ortografia do bot pro lancamento
6. Aba de creditos
7. Aba de invite do bot
8. SISTEMA MONETARIO (2021)
PREVISAO:
-Ate o final do mes de Novembro""")




    global embed_interacao
    embed_interacao = discord.Embed(title = "interacao", color = VERMELHO, description = r"""
$slap @
$hug @
$kiss @
$punch @
$pat @
$ascii @ - faz uma arte ascii com a foto de perfil da pessoa marcada
$casar @
$divorcio
$casado
""")


    global embed_pegarid
    embed_pegarid = discord.Embed(title = "Como pegar ID", color = VERMELHO, description = r"""
1. Va nas configuracoes
2. Va na aba "Aparencia" (No celular e na aba "comportamento")
3. Va em avancado (Se estiver no celular pule essa etapa)
4. Ative o modo desenvolvedor
5. Pra pegar o id de alguma pessoa, aperte com o botao direito no nome dela e selecione "Copiar Id" (No celular, apenas entre no perfil da pessoa e selecione a opcao "copiar Id")
6. Pronto! """)



    global embed_animais
    embed_animais = discord.Embed(title = "[+]----------Animais fofos----------[+]", color = VERMELHO, description = r"""
$cow
$cat
$dog
$pig
$fox
$koala""")

    global embed_cotacao
    embed_cotacao = discord.Embed(title = "[+]----------Moedas---------[+]", color = VERMELHO, description = r"""
$dolar - preco dolar (R$)
$euro - preco euro (R$)
$bitcoin - preco bitcoin (R$)
$litecoin - preco litecoin (R$)
$iene - preco iene japones (R$)
$etherium - preco etherium (R$)
$yuan - preco yuan chines (R$)
""")


    global embed_creditos
    embed_creditos = discord.Embed(title = "Creditos", color = VERMELHO, description = """
Bot feito por Whiz#6969
Algumas fotos foram pegas do instagram @boopmynose
    """)


    global embed_administracao
    embed_administracao = discord.Embed(title = "[+]----------Administracao----------[+]", color = VERMELHO, description = r"""
$ban @
$unban ID
$kick @
$membrosbanidos
$clear <QUANTIDADE>
$lock
$unlock
""")

    global embed_donate
    embed_donate = discord.Embed(title = "Donate", color = VERMELHO, description = """ MANUTENCAO
[+] Metodos:
$MercadoPago
""")

    global embed_mercadopago
    embed_mercadopago = discord.Embed(title = "Help", color = VERMELHO, description = r"""
[+] R$5,00: https://mpago.la/1Pumbnx
[+] R$10,00: https://mpago.la/15mkxzB
[+] R$15,00: https://mpago.la/1atgKES
[+] R$20,00: https://mpago.la/2Hr22sq
{{+}} Agradecemos!
""")


@client.event
async def on_member_join(member): #pra funcionar, precisa colocar os intents(client) e habilitar na pagina do bot(applications)
    print(f'{member} entrou no servidor {member.guild.name}')


@client.event
async def on_member_remove(member):
    print(f'{member} saiu do servidor {member.guild.name}')


@client.event
async def on_message(message):


    if message.content.lower().startswith('$help'):
        
        await message.channel.send(embed = embed_help)
        print(message.author,  " fez o comando $help no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$atts'):

        await message.channel.send(embed = embed_att)
        print(message.author,  " fez o comando $atts no canal:", message.channel, "no servidor:",  message.guild)
        

    if message.content.lower().startswith('$previsaoatts'):

        await message.channel.send(embed = embed_atts_prievistas)
        print(message.author,  " fez o comando $previsaoatts no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$animais'):

        await message.channel.send(embed = embed_animais)
        print(message.author,  " fez o comando $animais no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$cotacao'):

        await message.channel.send(embed = embed_cotacao)
        print(message.author,  " fez o comando $cotacao no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$creditos'):
        await message.channel.send(embed = embed_creditos)
        print(message.author,  " fez o comando $creditos no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$infccoins'):
        await message.channel.send(embed = embed_ccoins)
        print(message.author,  " fez o comando $ccoins no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$administracao'):

        await message.channel.send(embed = embed_administracao)
        print(message.author,  " fez o comando $administracao no canal:", message.channel, "no servidor:",  message.guild)


    if 'pedro' in message.content.lower():
        ale_pedro = random.randint(1, 1000)
        if ale_pedro == 3:
            await message.channel.send("Devolve o mamaco!")
            print(message.author,  " conseguiu o easter egg do macaco no canal:", message.channel, "no servidor:",  message.guild)
    

    if message.content.lower().startswith('$dog'):
        ale_dog = random.randint(1, 63)
        descricao_dog = random.choice(descricao_opc_dog)

        file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\animais\cachorro\0" + str(ale_dog) + ".jpg", filename="image.png")
        embed = discord.Embed(color = VERMELHO, title = descricao_dog)
        embed.set_image(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)

        #await message.channel.delete() DELETA O CANAL 
        #await message.delete() deleta so a msg
        print(message.author,  " fez o comando $dog no canal:", message.channel, "no servidor:",  message.guild)



    if message.content.lower().startswith('$cow'):
        ale_cow = random.randint(1, 11)

        file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\animais\vaca\0" + str(ale_cow) + ".jpg", filename="image.png")
        embed = discord.Embed(color = VERMELHO)
        embed.set_image(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)

        print(message.author,  " fez o comando $cow no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$cat'):
        ale_cat = random.randint(1, 6)
        descricao_cat = random.choice(descricao_opc_cat)

        file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\animais\gato\0" + str(ale_cat) + ".jpg", filename="image.png")
        embed = discord.Embed(color = VERMELHO, title = descricao_cat)
        embed.set_image(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)

        print(message.author,  " fez o comando $cat no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$pig'):
        ale_pig = random.randint(1, 15)
        easter = random.randint(1, 100000)


        file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\animais\porco\0" + str(ale_pig) + ".jpg", filename="image.png")
        embed = discord.Embed(color = VERMELHO, title = 'Oinc!')
        embed.set_image(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)
        print(message.author,  " fez o comando $pig no canal:", message.channel, "no servidor:",  message.guild)

        if easter == 3:
            embed_easter_rick = discord.Embed(color = VERMELHO, title = "Click!", description = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO")
            await message.channel.send(embed=embed_easter_rick)
            print(message.author,  " conseguiu o easter egg do porco no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$fox'):
        ale_fox = random.randint(1, 7)

        file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\animais\raposa\0" + str(ale_fox) + ".jpg", filename="image.png")
        embed = discord.Embed(color = VERMELHO)
        embed.set_image(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)

        print(message.author,  " fez o comando $fox no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$koala'):
        ale_coala = random.randint(1, 11)

        file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\animais\coala\0" + str(ale_coala) + ".jpg", filename="image.png")
        embed = discord.Embed(color = VERMELHO)
        embed.set_image(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)

        print(message.author,  " fez o comando $koala no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$donate'):

        await message.channel.send(embed = embed_donate)
        print(message.author,  " fez o comando $donate no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$mercadopago'):

        await message.channel.send(embed = embed_mercadopago)
        print(message.author,  " fez o comando $mercadopago no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$euro'):
            requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/EUR')

            cotacao = json.loads(requisicao.text)
            msg0 = "Preco euro: R$" + cotacao['EUR'] ['bid']

            await message.channel.send(msg0)
            print(message.author,  " fez o comando $euro no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$dolar'):
            requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/USD')

            cotacao = json.loads(requisicao.text)
            msg1 = "Preco dolar: R$" + cotacao['USD'] ['bid']

            await message.channel.send(msg1)
            print(message.author,  " fez o comando $dolar no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$bitcoin'):
            requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/BTC')

            cotacao = json.loads(requisicao.text)
            msg2 = "Preco bitcoin: R$" + cotacao['BTC'] ['bid']

            await message.channel.send(msg2)
            print(message.author,  " fez o comando $bitcoin no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$litecoin'):
            requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/LTC')

            cotacao = json.loads(requisicao.text)
            msg3 = "Preco litecoin: R$" + cotacao['LTC'] ['bid']

            await message.channel.send(msg3)
            print(message.author,  " fez o comando $litecoin no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$iene'):
            requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/JPY')

            cotacao = json.loads(requisicao.text)
            msg4 = "Preco Iene japones: R$" + cotacao['JPY'] ['bid']

            await message.channel.send(msg4)
            print(message.author,  " fez o comando $iene no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('$etherium'):
            requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/ETH')

            cotacao = json.loads(requisicao.text)
            msg5 = "Preco etherium: R$" + cotacao['ETH'] ['bid']

            await message.channel.send(msg5)
            print(message.author,  " fez o comando $etherium no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('$yuan'):
            requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/CNY')

            cotacao = json.loads(requisicao.text)
            msg6 = "Preco Yuan chines: R$" + cotacao['CNY'] ['bid']

            await message.channel.send(msg6)
            print(message.author,  " fez o comando $yuan no canal:", message.channel, "no servidor:",  message.guild)



    if message.content.lower().startswith('$ban') and message.author.guild_permissions.ban_members:

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        if "  " in msg:
            msg = msg.replace('  ', ' ')

        args = msg.split(' ')

        embed_ban = discord.Embed(title = "Banido(a)", color = VERMELHO, description = f"""
                                                                        Voce foi banido(a) do servidor {message.guild}.""")

        if len(args) == 2:
            #member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

        else:
            await message.channel.send('Voce precisa especificar o membro que quer kickar. $ban <membro>')

            try:
                if member:
                    user = client.get_user(member.id)
                    try:
                        await user.send(embed=embed_ban)
                    except Exception:
                        pass

                    await member.ban()
                    await message.channel.send(f'<@{member.id}> foi banido(a).')
                    print(message.author,  " fez o comando $ban no canal:", message.channel, "no servidor:",  message.guild, "e baniu", args[1])

                else:
                    await message.channel.send(f'Hmm... nao consegui achar um membro com o id {args[1]}...')

            except Exception:
                pass
    

    if message.content.lower().startswith('$unban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')

        if len(args) == 2:
            user = discord.utils.find(lambda m: args[1] in str(m.user.id), await message.guild.bans()).user

            if user:
                await message.guild.unban(user)
                await message.channel.send(f'<@{user.id}> foi desbanido(a).')
                print(message.author,  " fez o comando $unban no canal:", message.channel, "no servidor:",  message.guild, "e desbaniu", user.id)

            else:
                await message.channel.send(f'Nenhum membro banido com o id {args[1]} encontrado.')
    


    if message.content.lower().startswith('$kick') and message.author.guild_permissions.kick_members:


        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        elif "  " in msg: 
            msg = msg.replace('  ', ' ')

        args = msg.split(' ')

        embed_kick = discord.Embed(title = "Kickado(a)", color = VERMELHO, description = f"""
                                                                        Voce foi kickado(a) do servidor {message.guild}.""")

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members) #Kick por id
        
        else:
            await message.channel.send('Voce precisa especificar o membro que quer kickar. $kick <membro>')

        try:
            if member:
                    user = client.get_user(member.id)
                    try:
                        await user.send(embed=embed_kick)
                    except Exception:
                        pass

                    await member.kick()
                    await message.channel.send(f'<@{args[1]}> foi kickado(a).') #marca a pessoa
                    print(message.author,  " fez o comando $kick no canal:", message.channel, "no servidor:",  message.guild, "e kickou", args[1])

            else:
                await message.channel.send(f'Hmm... Nao consegui encontrar o id {args[1]}...')

        except Exception:
            pass


    if message.content.lower().startswith('$membrosbanidos') and message.author.guild_permissions.ban_members:
        membros_banidos = await message.guild.bans()

        for membros in membros_banidos:
            print(membros)
            await message.channel.send(f' ```{membros}``` ')

        if not membros_banidos:
            await message.channel.send("Nao existem membros banidos nesse servidor!")


    if message.content.lower().startswith('$mute'):
        #print(dir(message.author.guild_permissions))
        if message.author.guild_permissions.manage_roles:
            #print(dir(message.guild))
            #return
            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg: 
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

            else:
                await message.channel.send(f'<@{message.author.id}>, voce precisa mencionar alguem pra mutar!')
                return

            
            if member:
                try:
                    if get(message.guild.roles, name="🚫Cute-mute🚫"):
                        #await message.channel.send("Cargo mute ja existe")
                        role = discord.utils.get(message.guild.roles, name="🚫Cute-mute🚫")
                        perms = discord.Permissions(send_messages=False, read_messages=True)
                        await member.add_roles(role)
                        #await message.channel.set_permissions(message.guild.get_role('🚫Cute-mute🚫'), send_messages=False)
                        await message.channel.set_permissions(role, send_messages=False)
                        await message.channel.send(f'Ok, ok, <@{message.author.id}>, mutei o <@{args[1]}>. Tava badernando ai? ')

                    else:
                        guild = message.channel.guild
                        perms = discord.Permissions(send_messages=False, read_messages=True)
                        await guild.create_role(name="🚫Cute-mute🚫", permissions=perms)
                        role = discord.utils.get(message.guild.roles, name="🚫Cute-mute🚫")

                        await member.add_roles(role)
                        await message.channel.set_permissions(role, send_messages=False)
                        await message.channel.send(f'Ok, ok, <@{message.author.id}>, mutei o <@{args[1]}>. Tava badernando ai? ')

                except Exception:
                    await message.channel.send(f'Por algum motivo eu nao estou conseguindo mutar o(a) <@{member.id}>... Por acaso eu tenho permissao pra isso?')
                    pass
            else:
                await message.channel.send('Nao encontrei ninguem com esse nome aqui, sertifique-se que ele esta no servidor!')

        else:
            await message.channel.send(f'<@{message.author.id}>, voce nao tem permissao pra usar esse comando!')



    if message.content.lower().startswith('$unmute'):
        if message.author.guild_permissions.manage_roles:
            #print(dir(message.guild))
            #return
            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg: 
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

            else:
                await message.channel.send(f'<@{message.author.id}>, voce precisa mencionar alguem pra desmutar!')
                return

            if member:
                try:
                    role = discord.utils.get(message.guild.roles, name="🚫Cute-mute🚫")
                    await member.remove_roles(role)
                    await message.channel.send(f'Pronto, <@{message.author.id}>! Desmutei o <@{member.id}>!')
                
                except Exception:
                    await message.channel.send(f'Por algum motivo eu nao estou conseguindo mutar o(a) <@{member.id}>... Por acaso eu tenho permissao pra isso?')
                    pass
            else:
                await message.channel.send('Nao encontrei ninguem com esse nome por aqui, sertifique-se que ele ainda esta no server.')
        else:
            await message.channel.send('Voce nao tem permissao pra usar esse comando!')


    if message.content.lower().startswith('$lock'):
        if message.author.guild_permissions.manage_channels:
            overwrite = message.channel.overwrites_for(message.guild.default_role)
            overwrite.send_messages = False
            await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
            await message.channel.send(f'Ok, <@{message.author.id}>. Lockei o canal. TInha muita gente fazendo baderna? 🧐')
            #print(dir(message.author.guild_permissions))
        else:
            await message.channel.send(f'<@{message.author.id}>, voce nao tem permissao pra usar esse comando!')
    
    
    if message.content.lower().startswith('$unlock'):
        if message.author.guild_permissions.manage_channels:
            overwrite = message.channel.overwrites_for(message.guild.default_role)
            overwrite.send_messages = True
            await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
            await message.channel.send(f'Ja deslockei o canal, <@{message.author.id}> 👌👌')
        else:
            await message.channel.send(f'<@{message.author.id}>, voce nao tem permissao pra usar esse comando!')



    if message.content.lower().startswith('$comopegarid'):
        await message.channel.send(embed = embed_pegarid)
        print(f'{message.author} fez o comando $pegarid no chat {message.channel} no server {message.channel.guild}')



    if message.content.lower().startswith('$interacao'):
        await message.channel.send(embed = embed_interacao)
        print(f'{message.author} fez o comando $interacao no chat {message.channel} no server {message.channel.guild}')



    if message.content.lower().startswith('$slap'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')

        global ale_slap
        ale_slap = random.randint(1, 6)

        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

        
        if member:
            if member == message.author:
                await message.channel.send("Voce nao pode se tapear!")
                print(f'{message.author} tentou se tapear no canal {message.channel} no server {message.channel.guild}')
                return
            await message.channel.send(f"<@{message.author.id}> deu um tapa em <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_slap))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\aslap\0' + str(ale_slap) + '.gif'))
            print(f'{message.author} deu um tapa em {member} no canal {message.channel} no server {message.channel.guild}')
            
            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.channel.send("Nossa man")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')



    if message.content.lower().startswith('$hug'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')

        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

        
        if member:
            if member == message.author:
                await message.channel.send("Voce nao pode se abracar!")
                print(f'{message.author} tentou se abracar no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_hug = random.randint(1, 7)
            await message.channel.send(f"<@{message.author.id}> abracou <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_hug))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\hug\0' + str(ale_hug) + '.gif'))
            print(f'{message.author} abracou {member} no canal {message.channel} no server {message.channel.guild}')

            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.add_reaction(r"😊")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')


    if message.content.lower().startswith('$pat'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')

        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

        
        if member:
            if member == message.author:
                await message.channel.send("Voce nao pode se fazer carinho!!")
                print(f'{message.author} tentou se fazer carinho no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_pat = random.randint(1, 12)
            await message.channel.send(f"<@{message.author.id}> fez carinho em <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_pat))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\pat\0' + str(ale_pat) + '.gif'))
            print(f'{message.author} fez carinho em {member} no canal {message.channel} no server {message.channel.guild}')

            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.add_reaction(r"😊")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')





    if message.content.lower().startswith('$kiss'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')

        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

        
        if member:
            if member == message.author:
                await message.channel.send("Voce nao pode se beijar!")
                print(f'{message.author} tentou se beijar no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_kiss = random.randint(1, 9)
            await message.channel.send(f"<@{message.author.id}> beijou <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_kiss))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\kiss\0' + str(ale_kiss) + '.gif'))
            print(f'{message.author} beijou {member} no canal {message.channel} no server {message.channel.guild}')

            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.add_reaction(r"😳")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')






    if message.content.lower().startswith('$punch'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')


        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

#        if  == r"botest#7787":
#            print('teste')
        
        if member:

            if member == message.author:
                await message.channel.send("Voce nao pode se bater!")
                print(f'{message.author} tentou se bater no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_punch = random.randint(1, 7)
            await message.channel.send(f"<@{message.author.id}> bateu em <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_punch))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\punch\0' + str(ale_punch) + '.gif'))
            print(f'{message.author} bateu em {member} no canal {message.channel} no server {message.channel.guild}')


            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.channel.send(r"'-'")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')



    if message.content.lower().startswith('$ccoins'):

        with open('amounts.json') as f:
            amounts = json.loads(f.read())

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')
        msg = msg.replace('  ', ' ')

        if "&" in msg:
            msg = msg.replace('&', '')

        elif "  " in msg:
            msg = msg.replace('  ', ' ')

        args = msg.split(' ')

        if len(args) == 2:
            id = args[1]
            id = str(id)

            if id in amounts:
                await message.channel.send(f"<@{args[1]}> tem {amounts[id]} ccoins.")
                return

            else:
                await message.channel.send(f"<@{args[1]}> nao tem uma conta no banco.")
                return
        
        id = message.author.id
        id = str(id)

        if id in amounts:
            await message.channel.send("Voce tem {} ccoins na sua conta.".format(amounts[id]))

        else:
            await message.channel.send("Voce nao tem uma conta.")



    if message.content.lower().startswith('$registrar'):

        #print(dir(message.author))
        #await message.channel.send(message.author.avatar_url)
        #await message.channel.send(message.author.created_at)


        with open('amounts.json') as f:
            amounts = json.loads(f.read())

        with open('casais.json') as c:
            casais = json.loads(c.read())

        with open('ddiamond.json') as d:
            amounts_ddiamonds = json.loads(d.read())

        #amounts = ler_amounts()

        #print(amounts)

        #amounts = json.loads('amounts.json')

        id = message.author.id
        id = str(id)

        if id not in amounts_ddiamonds:
            amounts_ddiamonds[id] = 0
            _save_ddiamonds(amounts_ddiamonds)

        if id not in casais:
            casais[id] = 100
            await message.channel.send("Agora voce esta registrado no cartorio.")
            _casaisSave(casais)

        elif id in casais:
            await message.channel.send("Voce ja e registrado no cartorio. Voce ja pode casar.")

        if id not in amounts:
            amounts[id] = 100
            await message.channel.send("Agora voce esta registrado. Te dei 100 ccois de brinde :D")
            _save(amounts)

        elif id in amounts:
            await message.channel.send("Voce ja tem uma conta no banco!")

        _save(amounts)
        #print(amounts)


    if message.content.lower().startswith('$transferir'):

            with open('amounts.json') as f:
                amounts = json.loads(f.read())

            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')
            msg = msg.replace('  ', ' ')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg:
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')
            other_id = args[2]
            other_id = str(other_id)

            amount = args[1]

            primary_id = message.author.id
            primary_id = str(primary_id)

            if primary_id not in amounts:
                await message.channel.send("Voce nao tem uma conta. Utilize o comando $registrar para prosseguir.")

            elif other_id not in amounts:
                await message.channel.send("Teu colega n tem uma conta")

            elif amounts[primary_id] < int(amount):
                await message.channel.send("Vc n tem tudo isso n ou")

            else:
                amounts[primary_id] -= int(amount)
                amounts[other_id] += int(amount)
                await message.channel.send("Transacao completa!")

            _save(amounts)



    if message.content.lower().startswith('$ddiamonds'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')
        msg = msg.replace('  ', ' ')

        if "&" in msg:
            msg = msg.replace('&', '')

        elif "  " in msg:
            msg = msg.replace('  ', ' ')

        args = msg.split(' ')

        with open('ddiamond.json') as d:
            amounts_ddiamonds = json.loads(d.read())

        global id_Autor
        id_Autor = str(message.author.id)

        if len(args) == 2:
            marcado = str(args[1])
            if marcado in amounts_ddiamonds:
                await message.channel.send(f'<@{marcado}> tem {amounts_ddiamonds[marcado]} ddiamonds.')
            else:
                await message.channel.send(f'<@{marcado}> nao esta registrado.')

        else:
            if id_Autor in amounts_ddiamonds:
                await message.channel.send(f"Voce tem {amounts_ddiamonds[id_Autor]} ddiamonds.")
            
            else:
                await message.channel.send("Voce nao esta registrado. Use o comando $registrar.")




    if message.content.lower().startswith("$prcddiamond"):
        await message.channel.send(f'Preco de 1 ddiamond: {int(preco_ddiamond())} ccoins.')
        await message.channel.send('Voce pode comprar ddiamonds pelo comando $buyddiamond')


    if message.content.lower().startswith('$buyddiamond'):
        with open('amounts.json') as f:
            amounts = json.loads(f.read())

        with open('ddiamond.json') as d:
            amounts_ddiamonds = json.loads(d.read())

        global message_sent
        message_sent = message

        id_Autor = str(message.author.id)
        preco = int(preco_ddiamond())

        if id_Autor in amounts:
            if amounts[id_Autor] >= preco:
                msg_compra = await message.channel.send(f'<@{id_Autor}> | Voce esta prestes a comprar 1 ddiamond por {preco} ccoins. Tem certeza que quer finalizar a transacao?')

                await msg_compra.add_reaction('✅')
                await msg_compra.add_reaction('❌')

                #msg_compra_id = msg_compra.id
                
            else:
                await message.channel.send('Voce nao tem ccoins suficientes para comprar um ddiamond.')
        else:
            await message.channel.send('Voce nao esta registrado. Use o comando $registrar para continuar.')


    
    if message.content.lower().startswith('$sellddiamond'):
        with open('amounts.json') as f:
            amounts = json.loads(f.read())

        with open('ddiamond.json') as d:
            amounts_ddiamonds = json.loads(d.read())

        global message_sent_sell
        message_sent_sell = message

        id_Autor = str(message.author.id)

        preco = int(preco_ddiamond())

        if id_Autor in amounts:
            if amounts_ddiamonds[id_Autor] >= 1:
                msg_venda = await message.channel.send(f'<@{id_Autor}> | Voce esta prestes a vender 1 ddiamond por {preco} ccoins. Tem certeza que quer finalizar a transacao?')

                await msg_venda.add_reaction('❎')
                await msg_venda.add_reaction('🚫')

                #msg_venda_id = msg_venda.id

            else:
                await message.channel.send('Voce nao tem ddiamonds pra vender!')
        else:
            await message.channel.send('Voce nao esta registrado. Use o comando $registrar para continuar.')



    if message.content.lower().startswith('$clear'):
        if message.author.guild_permissions.manage_channels:
            
            msg = message.content.replace('  ', ' ')
            
            args = msg.split(' ')

            if len(args) == 2:

                quantidade = args[1]
                quantidade = int(quantidade)

                if quantidade > 100 or quantidade <= 1:
                    await message.channel.send('Eu so apago entre 2 e 100 mensagens!', delete_after = 5)

                else:
                    await message.channel.purge(limit=quantidade)
                    await message.channel.send(f'O chat foi limpo por <@{message.author.id}>!', delete_after = 5)

        else:
            await message.channel.send(f'<@{message.author.id}> voce nao tem permissao para usar esse comando!')



    if message.content.lower().startswith('$ping'):
     #   await message.channel.send("Eu estou em " + str(len(client.servers)) + " servers")
        await message.channel.send(f"Estou com {client.latency}ms.")


    if message.content.lower().startswith('$userinfo'):

            with open('casais.json') as c:
                casais = json.loads(c.read())

            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')
            msg = msg.replace('  ', ' ')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg:
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

                if member:
                    embed_userinfo = discord.Embed(Title="Informacoes de usuario", color = VERMELHO)
                    if args[1] in casais and casais[args[1]] != 100:
                        casado = f'Casado(a) com <@{casais[args[1]]}>'
                    else:
                        solteiro = f'<@{member.id}> esta solteiro!'

                    if args[1] in casais and casais[args[1]] != 100:
                        embed_userinfo.add_field(name="Casado/solteito", value= casado, inline=True)

                    else:
                        embed_userinfo.add_field(name='Casado/solteiro', value=solteiro, inline=True)

                    embed_userinfo.add_field(name="Usuario", value=member, inline=True)
                    embed_userinfo.add_field(name="Id", value=member.id, inline=True)
                    embed_userinfo.add_field(name="Status", value=f"{member.activity}", inline=True)
                    embed_userinfo.add_field(name="Entrou no servidor em", value=member.joined_at.strftime("%b %d, %Y"), inline=True)
                    embed_userinfo.add_field(name="Conta criada em", value=member.created_at.strftime("%b %d, %Y"), inline=True)
                    embed_userinfo.set_image(url=member.avatar_url)

                    await message.channel.send(embed=embed_userinfo)
                else:
                    await message.channel.send('Hmmm... Nao consegui encontrar esse membro do servidor...')

            else:
                await message.channel.send("Voce precisa marcar alguem para ver as informacoes dela.")


    if message.content.lower().startswith('$serverinfo'):

        membros = message.channel.guild.members
        membros = len(membros)

        regiao = message.channel.guild.region

        embed_serverinfo = discord.Embed(title=f"Informacoes do servidor {message.channel.guild.name}", color = VERMELHO)

        embed_serverinfo.add_field(name='Dono', value=f"{message.channel.guild.owner}", inline=True)
        embed_serverinfo.add_field(name='Id do dono', value=f"{message.channel.guild.owner.id}", inline=True)
        embed_serverinfo.add_field(name='Regiao do servidor', value=f"{regiao}", inline=True)
        embed_serverinfo.add_field(name='Membros', value=f"{membros}", inline=True)
        embed_serverinfo.add_field(name="Servidor criado em", value=f"{message.channel.guild.created_at.strftime('%b %d, %Y')}", inline=True)
        embed_serverinfo.add_field(name='Id do servidor', value=f"{message.channel.guild.id}", inline=True)
        #embed_serverinfo.set_image(url=message.channel.guild.banner_url)
        embed_serverinfo.set_image(url=message.channel.guild.icon_url)
        
        await message.channel.send(embed=embed_serverinfo)


    if message.content.lower().startswith('$casar'):

            with open('casais.json') as c:
                casais = json.loads(c.read())

            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')
            msg = msg.replace('  ', ' ')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg:
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            if len(args) == 2:
                

                global idMarcado
                idMarcado = args[1]
                global idAutor
                idAutor = message.author.id

                message_sent = message

                if int(idMarcado) == message.author.id:
                    await message.channel.send('Voce nao pode casar com voce mesmo!')
                    return

                if idMarcado in casais and casais[idMarcado]:

                    if str(idAutor) not in casais:
                        await message.channel.send("Voce nao esta registrado no cartorio. Use o comando $registrar.")
                        return

                    elif idAutor in casais and casais[idAutor] != 100:
                        await message.channel.send(f"Ouou!? Tu e casado com <@{casais[idAutor]}>. Ta loko?")
                        return
                    

                    elif casais[idMarcado] == 100:
                        global mensagem
                        mensagem = await message.channel.send(embed=embed_casamento1, delete_after = 30)

                        global msg_id
                        msg_id = mensagem.id

                        #casais[idAutor] = None
                        #casais[idMarcado] = None

                        await mensagem.add_reaction('❤️')
                        await mensagem.add_reaction('💔')
                        return


                    if str(casais[idMarcado]) == str(idAutor):
                        await message.channel.send('Voce ja e casado com essa pessoa.')
                        return

                    if str(casais[idMarcado]) != str(idAutor):
                        await message.channel.send(f"Ououou!? Ta talaricando ai? <@{idMarcado}> ja e casado(a) com <@{casais[idMarcado]}>!")
                        #print(args[1], idMarcado)
                        return


                elif str(idAutor) not in casais:
                    await message.channel.send("Voce nao esta registrado no cartorio. Use o comando $registrar.")
                    return

                elif str(idMarcado) not in casais:
                    #print(str(idMarcado))
                    #print(casais[idAutor], casais[idMarcado])
                    await message.channel.send('O(a) seu companheiro nao esta registrado no cartorio. Use o comando $registrar.')
                    return


    if message.content.lower().startswith('$casado') or message.content.lower().startswith('$casada'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')
        msg = msg.replace('  ', ' ')

        if "&" in msg:
            msg = msg.replace('&', '')

        elif "  " in msg:
            msg = msg.replace('  ', ' ')

        args = msg.split(' ')
        print(args)
        #print(args[1])

        with open('casais.json') as c:
            casais = json.loads(c.read())

        if len(args) == 2:
            idMarcado = args[1]
            idMarcado = str(idMarcado)
            if idMarcado in casais and casais[idMarcado] != 100:
                await message.channel.send(f'<@{idMarcado}> esta casado(a) com <@{casais[idMarcado]}>!')

            else:
                await message.channel.send(f'<@{idMarcado}> nao esta casado(a)!')

        else:

            idAutor = message.author.id
            idAutor = str(idAutor)
            if idAutor in casais and casais[idAutor] != 100:
                await message.channel.send(f'Voce e casado(a) com <@{casais[idAutor]}>.')

            else:
                await message.channel.send('Voce nao e casado(a)!')



    if message.content.lower().startswith('$divorcio'):

        global msg_id_divorcio
        message_sent = message
        idAutor = message.author.id

        #global idAutor
        #global idMarcado

        with open('casais.json') as c:
            casais = json.loads(c.read())

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')
        msg = msg.replace('  ', ' ')

        if "&" in msg:
            msg = msg.replace('&', '')

        elif "  " in msg:
            msg = msg.replace('  ', ' ')

        args = msg.split(' ')

        if str(idAutor) in casais and casais[str(idAutor)] and casais[str(idAutor)] != 100:
            mensagem = await message.channel.send(embed=embed_divorcio)
            msg_id_divorcio = mensagem.id
            await mensagem.add_reaction('👋')
            return
        
        else:
            await message.channel.send('Voce nao e casado com ninguem!')



    if message.content.lower().startswith('$ascii'):

            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')
            msg = msg.replace('  ', ' ')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg:
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            if len(args) == 2:

                mensagem = await message.channel.send('Ok, talvez isso demore alguns segundos. E meio complicado trabalhar com isso. :smile:')
                
                filename = "avatar1.jpg"

                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

                try:
                    await member.avatar_url.save(filename)
                except Exception:
                    await message.channel.send('Voce tem que marcar alguem ou usar o id dela. Exemplo: $ascii @pessoa_qualquer. (Ela precisa estar no server.)')
                    return

                #file = discord.File(fp=filename)
                #await message.channel.send("Enjoy :>", file=file)
                asciiBot.main()
                file = discord.File(fp = 'ascii_image.txt')
                #time.sleep(5)
                await mensagem.delete()
                await message.channel.send(file=file)
                os.remove('ascii_image.txt')
                os.remove('avatar1.jpg')

            else:
                await message.channel.send('Voce tem que marcar alguem ou usar o id dela. Exemplo: $ascii @pessoa_qualquer. (Ela precisa estar no server.)')



@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "❤️" and msg.id == msg_id and str(user.id) == str(idMarcado):
        ale_casamento = random.choice(strings.lista_casamento)

        with open('casais.json') as c:
            casais = json.loads(c.read())

        #file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\acoes\casamento\0" + str(ale_casamento) + ".gif", filename="image.gif")
        #embed = discord.Embed(color = VERMELHO, title = "Casados! Parabens pelo casal!", description = "Agora, seu casamento ficara registrado para todos verem ate alguem pedir $divorcio.")
        #embed.set_image(url="attachment://image.gif")

        #anuncio_casamento = await message_sent.channel.send(file=file, embed=embed)

        await message_sent.channel.send('Casados! Parabens pelo casal! Agora, seu casamento ficara registrado para todos verem ate alguem pedir $divorcio.')
        anuncio_casamento = await message_sent.channel.send(ale_casamento)

        with open('casais.json', 'rb') as source_file:
            stringAuthorId = str(idAutor)
            for line in source_file:
                element = json.loads(line.strip())
                #print(element)
                #print(casais)
                #print('teste1')
                if str(stringAuthorId) in element and element[stringAuthorId] == 100:
                    #print('teste2')
                    #print(element[stringAuthorId])
        
                    del casais[stringAuthorId]
                    #element.pop(stringAuthorId, None)
        
                    #print('teste3')

                _casaisSave(casais)

        casais[idAutor] = str(idMarcado)
        _casaisSave(casais)
        casais[idMarcado] = str(idAutor)
        _casaisSave(casais)

        
        await anuncio_casamento.add_reaction("🎉")

        await mensagem.delete()


    if reaction.emoji == "💔" and msg.id == msg_id and str(user.id) == str(idMarcado):

        ale_slap = random.randint(1, 6)
        file = discord.File(r"C:\Users\Leonardo\Desktop\bot animais\acoes\aslap\0" + str(ale_slap) + ".gif", filename="image.gif")
        embed = discord.Embed(color = VERMELHO, title = "Rejeitado!", description = "Que q isso soldado, boa sorte da proxima vez. (sem ideias p ca)")
        embed.set_image(url="attachment://image.gif")
        anuncio_casamento_rejeitado = await message_sent.channel.send(file=file, embed=embed)
        
        await anuncio_casamento_rejeitado.add_reaction('😢')

        await mensagem.delete()


    if reaction.emoji == "👋" and msg.id == msg_id_divorcio and str(idAutor) == str(user.id):

        with open('casais.json') as c:
            casais = json.loads(c.read())

        with open('casais.json', 'rb') as source_file:
            stringAuthorId = str(idAutor)
            for line in source_file:
                element = json.loads(line.strip())
                #print(element)
                if str(stringAuthorId) in element and element[stringAuthorId] != 100:
                    #print(element[str(idAutor)])
        
                    #del casais[stringAuthorId]
                    #marcado = element[stringAuthorId]
                    marcado = element[str(idAutor)]

                    autor = element[str(marcado)]

                    del casais[marcado]
                    casais[marcado] = 100
                    _casaisSave(casais)

                    del casais[autor]
                    casais[autor] = 100
                    _casaisSave(casais)

                _casaisSave(casais)
        
        await message_sent.channel.send('Voces eram tao lindos juntos... Mas vida que segue :sleepy:')
        await mensagem.delete()
        return

    
    if reaction.emoji == "✅" and id_Autor == str(user.id):
        with open('amounts.json') as f:
            amounts = json.loads(f.read())

        with open('ddiamond.json') as d:
            amounts_ddiamonds = json.loads(d.read())


        amounts[id_Autor] -= preco
        amounts_ddiamonds[id_Autor] += 1
        _save(amounts)
        _save_ddiamonds(amounts_ddiamonds)
         
        await message_sent.channel.send('Transacao concluida.')
        return



    if reaction.emoji == "❌" and id_Autor == str(user.id):
        await message_sent.channel.send('Ta bom entao ne... Concordo que esteja um pouco caro...')
        return




    if reaction.emoji == "❎" and id_Autor == str(user.id):
        with open('amounts.json') as f:
            amounts = json.loads(f.read())

        with open('ddiamond.json') as d:
            amounts_ddiamonds = json.loads(d.read())


        amounts[id_Autor] += preco
        amounts_ddiamonds[id_Autor] -= 1
        _save(amounts)
        _save_ddiamonds(amounts_ddiamonds)
         
        await message_sent.channel.send('Transacao concluida.')
        return



    if reaction.emoji == "🚫" and id_Autor == str(user.id):
        await message_sent.channel.send('ok')
        return

#token = base.decc("TnpZNE16QTNOVGt4TlRJek5UazRNelUyLlg0LWtOQS5QalBDVmo3ZFg2d1RJMS1QX2dzZGJMdmh5MGs=") #cuteannibot, mas oculto

client.run("NzY4MzA3NTkxNTIzNTk4MzU2.GTlJBe.etx_8kgSu3RPnZU3zDqRxq9Ty_sk-7Bcb_Yyrc") #cuteannibot