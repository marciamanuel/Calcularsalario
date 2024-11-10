from fpdf import FPDF
import os

print("Cálculo para saber o Salário Liquido de um funcionário")
print("="*30)
nome=(input("Digite o seu nome completo\n"))
salario=float(input("Digite o seu salário base\n"))
subsidio_Al=float(input("Digite o seu subsidio de alimentação\n"))
subsidio_T=float(input("Digite o seu subsidio de transporte\n"))
subsidio_S=float(input("Digite o seu subsidio de saúde\n"))
subsidio_R=float(input("Digite o seu subsidio de risco\n"))
subsidio_A=float(input("Digite o seu subsidio de atavio\n"))
n_F=int(input("Digite o seu número de faltas\n"))





s_bruto=salario+subsidio_Al+subsidio_T+subsidio_S+subsidio_R+subsidio_A

print(" O seu salário bruto é :{:,.2f}\n".format(s_bruto))

s_s=s_bruto*0.03
print(" O valor da segurança social é :{:,.2f}\n".format(s_s))

if subsidio_Al and subsidio_T>30000:
    s_restoA=subsidio_Al-30000
    s_restoT=subsidio_T-30000
    
    mci=salario-s_s+subsidio_S+subsidio_R+subsidio_A+s_restoT+s_restoA
    print(" O valor da matéria coletável é :{:,.2f}\n".format(mci))
elif subsidio_Al>30000:
        s_restoA=subsidio_Al-30000

        mci=salario-s_s+subsidio_S+subsidio_R+subsidio_A+s_restoA
        print(" O valor da matéria coletável é :{:,.2f}\n".format(mci))
elif subsidio_T>30000:
    s_restoT=subsidio_T-30000

    mci=salario-s_s+subsidio_S+subsidio_R+subsidio_A+s_restoA
    print(" O valor da matéria coletável é :{:,.2f}\n".format(mci))
else:     
    s_restoT=subsidio_T-30000
    mci=salario-s_s+subsidio_S+subsidio_R+subsidio_A+s_restoT
    print(" O valor da matéria coletável é :{:,.2f}\n".format(mci))

print("Cálculo para saber o IRT de um funcionário")
print("="*30)

if mci<=100000:
    irt=0
    print(" O valor IRT é :{:,.2f}\n".format(irt))

elif 100000 < mci <= 150000:
    irt=0+(mci-100000)*0,13
    print(" O valor IRT é :{:,.2f}\n".format(irt))

elif 150000 < mci <= 200000:
    irt = 12500 + (mci - 150000) * 0.16
    print(" O valor IRT é :{:,.2f}\n".format(irt))

elif 200000 < mci <= 300000:
    irt = 31250 + (mci - 200000) * 0.18
    print(" O valor IRT é :{:,.2f}\n".format(irt))

elif 300000 < mci <= 500000:
    irt = 49250 + (mci - 300000) * 0.19
    print(" O valor IRT é :{:,.2f}\n".format(irt)) 

elif 500000 < mci <= 1000000:
    irt = 87250 + (mci - 500000) * 0.20
    print(" O valor IRT é :{:,.2f}\n".format(irt))

elif 1000000 < mci <= 1500000:
    irt = 187249 + (mci - 1000000) * 0.21
    print(" O valor IRT é :{:,.2f}\n".format(irt))

elif 1500000 < mci <= 2000000:
    irt = 292249 + (mci - 1500000) * 0.22
    print(" O valor IRT é :{:,.2f}\n".format(irt))  

elif 2000000 < mci <= 2500000:
    irt = 402249 + (mci - 2000000) * 0.23
    print(" O valor IRT é :{:,.2f}\n".format(irt))


elif 2500000 < mci <= 5000000:
    irt = 517249 + (mci - 2500000) * 0.245
    print(" O valor IRT é :{:,.2f}\n".format(irt))

elif mci >= 10000000:
    irt = 2342248 + (mci - 10000000) * 0.25
    print(" O valor IRT é :{:,.2f}\n".format(irt))     


else:
    irt = 157250 + (mci - 1000000) * 0.22


print("Cálculo para saber o desconto de um funcionário")
print("="*30)

df=s_bruto/22*n_F
print(" O valor do desconto de faltas é :\n",df)

td=s_s+irt+df
print(" O valor dos descontos é :\n",td)

print("Cálculo para saber o salário liquído de um funcionário")
print("="*30)

sl=s_bruto-td

print(" O salário liquido de",nome,"é:\n",sl)



# Função para gerar relatório com tabela centralizada
def gerar_relatorio_pdf(nome, salario, subsidio_Al, subsidio_T, subsidio_S, subsidio_R, subsidio_A, n_F, s_bruto, s_s, mci, irt, df, td, sl):
     # Instanciando o objeto FPDF no modo paisagem (L = Landscape)
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    
    # Adicionando uma página ao PDF
    pdf.add_page()

    # Título do relatório
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Relatório de Salário - {nome}", ln=True, align="C")
    pdf.ln(10)  # Espaço entre o título e a tabela

    # Definindo as colunas
    col1_width = 90  # Largura da primeira coluna
    col2_width = 50  # Largura da segunda coluna
    table_width = col1_width + col2_width  # Largura total da tabela

    # Calcular a posição horizontal para centralizar a tabela
    page_width = pdf.w - 2 * pdf.l_margin  # Largura da página (excluindo as margens)
    start_x = (page_width - table_width) / 2 + pdf.l_margin  # Posição inicial da tabela

    # Cabeçalhos da tabela
    pdf.set_font("Arial", "B", 12)
    pdf.set_x(start_x)  # Mover para a posição inicial
    pdf.cell(col1_width, 10, "Descrição", 1, 0, "C")
    pdf.cell(col2_width, 10, "Valor", 1, 1, "C")

    # Definindo a fonte para os dados
    pdf.set_font("Arial", "", 12)

    # Adicionando os dados à tabela
    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Salário Base", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{salario:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Subsidio Alimentação", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{subsidio_Al:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Subsidio Transporte", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{subsidio_T:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Subsidio Saúde", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{subsidio_S:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Subsidio Risco", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{subsidio_R:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Subsidio Atavio", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{subsidio_A:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Nº de Faltas", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{n_F}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Salário Bruto", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{s_bruto:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Segurança Social", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{s_s:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Matéria Coletável", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{mci:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "IRT", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{irt:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Desconto de Faltas", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{df:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Total de Descontos", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{td:.2f}", 1, 1, "C")

    pdf.set_x(start_x)
    pdf.cell(col1_width, 10, "Salário Líquido", 1, 0, "C")
    pdf.cell(col2_width, 10, f"{sl:.2f}", 1, 1, "C")




    pdf.output("/Users/Drfernandomateus/Documents/relatorio_salario.pdf")
    print("Relatório PDF gerado com sucesso!")

# Gerar o relatório PDF
gerar_relatorio_pdf(nome, salario, subsidio_Al, subsidio_T, subsidio_S, subsidio_R, subsidio_A, n_F, s_bruto, s_s, mci, irt, df, td, sl)









