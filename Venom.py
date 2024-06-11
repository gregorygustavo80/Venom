from pdf2docx import Converter
from docx2pdf import convert

def pdf_docx():
    try:
        pdf_file = input('Digite o caminho do seu arquivo pdf: ').strip().replace('"', '')
        docx_file = pdf_file.replace('.pdf', '.docx')
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        print(f'Conversão concluída: {docx_file}')
    except Exception as e:
        print(f'Erro ao converter documento: {e}')

def docx_pdf():
    try:
        docx_file = input('Digite o caminho do seu arquivo docx: ').strip().replace('"', '')
        pdf_file = docx_file.replace('.docx', '.pdf')
        convert(docx_file, pdf_file)
        print(f'Conversão concluída: {pdf_file}')
    except Exception as e:
        print(f'Erro ao converter documento: {e}')

def main():
    resposta = int(input('[1] PDF para Docx [2] Docx para pdf: '))
    
    if resposta == 1:
        pdf_docx()
    elif resposta == 2:
        print('É necessário ter o Word instalado. ')
        docx_pdf()
    else:
        print('Opção inválida.')

if __name__ == '__main__':
    main()
