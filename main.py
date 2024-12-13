from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import ttfonts
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import white, black, HexColor

pdfmetrics.registerFont(ttfonts.TTFont('Fonte1', 'C:\\windows\\fonts\\lucon.ttf'))
pdfmetrics.registerFont(ttfonts.TTFont('Fonte2', 'C:\\users\\M I L T O G R O\\appdata\\local\\microsoft\\windows\\fonts\\balance groovy - sans.ttf'))
pdfmetrics.registerFont(ttfonts.TTFont('Fonte3', 'C:\\users\\M I L T O G R O\\appdata\\local\\microsoft\\windows\\fonts\\mario-kart-ds.ttf'))

cnv = canvas.Canvas("cartas.pdf", pagesize=A4)
cnv.setFont("Fonte2", 8)

def criarCarta(cnv, x, y, xS, yS, tipo, nome, *dicas):
    cnv.drawImage("Art/card.png", x, y, width=xS, height=yS)
    
    margem = 10
    espaco_linha = 11.1

    texto_x = x + margem
    texto_y = y + yS - margem

    cnv.setFillColor(black)

    cnv.drawString(texto_x, texto_y - 6.5, f"{tipo}")

    cnv.setFillColor(white)
    cnv.drawString(texto_x + 85, texto_y - 6.5, f"{nome}")
    texto_y -= espaco_linha

    cnv.setFillColor(black)
    for i, dica in enumerate(dicas[:20], start=1):
        cnv.drawString(texto_x, texto_y - 5, f"{i}")
        cnv.drawString(texto_x + 12, texto_y - 5, f"{dica}")
        texto_y -= espaco_linha

x = 5
y = 590
xS = 190
yS = 245

# Linha 1
criarCarta(cnv, x, y, xS, yS,"Objeto", "Caneta","Usado para escrever", "Tem tinta", "Pode ser descartável","Existem modelos caros", "É uma ferramenta de escritório","Usado em escolas", "É cilíndrico", "Geralmente tem tampa","Pode ser recarregável", "Existem canetas esferográficas","Canetas podem ser personalizadas", "Varia de cor","Foi inventado há séculos", "É pequena", "Leve para carregar","Usada por escritores", "Ajuda em provas", "Barata para comprar","Comum no dia a dia", "Pode ser transparente ou colorido")
criarCarta(cnv, x + xS + x, y, xS, yS,"Animal", "Elefante","É grande", "Tem tromba", "Possui presas","Habita savanas e florestas", "É herbívoro", "Animal terrestre","Muito pesado", "Inteligente", "Tem boa memória","Um símbolo de força", "Pode viver mais de 60 anos","Presente na cultura asiática", "Animal ameaçado","Ajuda em transportes no passado", "Relacionado ao circo","Mamífero", "Existem em grupos", "Tem pele cinza","Habita África e Ásia", "Tem 5 'pernas'")
criarCarta(cnv, (x * 3) + (xS * 2), y, xS, yS,"Fruta", "Banana","É amarela", "Cresce em cachos", "Fonte de potássio","Pode ser comida crua", "Usada em sobremesas", "Existem várias espécies","Facilmente encontrada no mercado", "Popular no mundo inteiro","Ajuda na digestão", "Originária de climas tropicais","Pode ser frita", "Faz parte de receitas","Embalagem natural", "Leve para carregar","Doce naturalmente", "Muito nutritiva", "Barata para comprar","Um lanche saudável", "Comum no café da manhã", "Macaco ama")

# Linha 2
criarCarta(cnv, x, y - yS - (x * 5), xS, yS,"Objeto", "Relógio","Usado para ver horas", "Pode ser de pulso", "Também decorativo","Pode ter alarme", "É um presente comum", "Mede o tempo","Pode ser digital ou analógico", "Importante no trabalho","Existem modelos caros", "Alguns são resistentes à água","Usado em eventos esportivos", "Auxilia na pontualidade","Fabricado por grandes marcas", "Feito de vários materiais","Funciona a bateria ou corda", "Comum na rotina diária","Usado desde a antiguidade", "Facilita organização","Tecnologia embarcada", "Muito útil")
criarCarta(cnv, x + xS + x, y - yS - (x * 5), xS, yS,"Comida", "Pizza","É redonda", "Popular mundialmente", "Feita com massa","Tem molho de tomate", "Pode ter queijo", "Diversos sabores","Preparada em forno", "Usada em festas", "Pode ser congelada","É italiana", "Fácil de compartilhar", "Pode ser personalizada","Comida rápida", "Popular entre jovens", "Amada por crianças","Existem pizzas vegetarianas", "Pode ter borda recheada","Comida informal", "Presente em delivery", "Fácil de encontrar")
criarCarta(cnv, (x * 3) + (xS * 2), y - yS - (x * 5), xS, yS,"País", "Brasil","Está na América do Sul", "Tem a Amazônia", "País tropical","Famoso pelo futebol", "Tem o Cristo Redentor", "Maior país da América do Sul","Fala português", "Cultura rica", "Tem o carnaval","Famoso por praias", "Exporta café", "Tem diversidade cultural","Clima variado", "Independência em 1822", "Rico em minerais","Possui grandes rios", "Maior exportador de carne", "É multicultural","País turístico", "Tem belas paisagens naturais")

# Linha 3
criarCarta(cnv, x, y - (yS * 2) - (x * 10), xS, yS,"Objeto", "Computador","É eletrônico", "Usado para trabalhar", "Pode ser portátil","Serve para jogos", "Conecta à internet", "Armazena dados","É multitarefa", "Pode ser caro", "Usado em escritórios","É essencial atualmente", "Tem memória RAM", "Executa softwares","Pode ser desktop", "Possui tela", "Utiliza teclado e mouse","Usado por estudantes", "Ajuda em pesquisas", "Usado em projetos","Presente em casas", "Evolui constantemente")
criarCarta(cnv, x + xS + x, y - (yS * 2) - (x * 10), xS, yS,"Esporte", "Basquete","Jogado com bola", "Disputa em quadra", "Tem cestas","É coletivo", "Popular nos EUA", "Precisa de habilidade","Tem dribles", "Precisa de resistência", "Usa tabela","Objetivo é pontuar", "Regras específicas", "Tem torcedores","Existem ligas profissionais", "Usado em escolas", "Popular mundialmente","Tem times femininos", "Requer trabalho em equipe", "Originado no Canadá", "Muitos atletas altos", "Amado por fãs")
criarCarta(cnv, (x * 3) + (xS * 2), y - (yS * 2) - (x * 10), xS, yS, "Lugar", "Praia", "Tem areia", "Água do mar", "Local para relaxar", "Comum em climas tropicais", "Tem coqueiros", "Usado para férias", "Pode ter esportes aquáticos", "É turístico", "Lugar para nadar", "Tem ondas", "Pode ser movimentado", "Bom para famílias", "Tem barracas de comida", "Paisagem bonita", "Nascer do sol incrível", "Varia em tamanho", "É acessível em muitos países", "Relaxante", "Bom para esportes de areia", "Procurada por surfistas")


cnv.save()
