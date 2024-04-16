import PyPDF2
import re

def extract_cpf_from_pdf(pdf_path):
    cpf_list = []
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            # cpf_matches = re.findall(r'Cpf\s*:\s*(\d{11})', text)
            cpf_matches = re.findall(r'\b\d{11}\b', text)
            if cpf_matches:
                cpf_list.extend(cpf_matches)
    return cpf_list

def save_cpf_to_txt(cpf_list, txt_path):
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(cpf_list))

def main():
    pdf_path = "C:/Users/itarg/Downloads/estagio março.pdf"  # Substitua "exemplo.pdf" pelo caminho do seu arquivo PDF
    cpf_list = extract_cpf_from_pdf(pdf_path)
    print("CPFs extraídos do PDF:")
    print(cpf_list)

    txt_path = "cpfs_extraidos.txt"
    save_cpf_to_txt(cpf_list, txt_path)
    print(f"CPFs salvos em '{txt_path}'.")

if __name__ == "__main__":
    main()

    

