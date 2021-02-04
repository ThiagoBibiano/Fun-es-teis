import pandas as pd


def retorna_proxima_info(pasta, col_comparar, col_key, nome, sheet_name=0):
    """
    A função é feita para ler uma pasta excel
    
    Retorna uma lista com o próximo item em relação ao indice de um 'nome',
    que é inserido na variável de mesma alcunha, sendo que, se o nome não 
    aparecer no campo em questão, ele ignora o retorno
    """
    
    
    df = pd.read_excel(pasta, sheet_name)
    lista = []
    
    for i in range(df.last_valid_index()+1):
        if nome in df[col_comparar][i]:
            df_list = df[col_comparar][i].split()
            
            for count, wrd in enumerate(df_list):
                if nome == wrd:
                    try: lista.append((df[col_key][i],df_list[count+1]))
                    except: continue
    return lista
