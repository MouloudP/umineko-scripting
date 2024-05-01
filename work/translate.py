def fFoundCharID(sLine):
    # Trouver l'index du 1er caractère de l'alphabet dans la ligne en partant du début

    nStart = 0
    for i in range(len(sLine)):
        if sLine[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàéiôèuÀÉIÖÜàéiôèu":
            nStart = i
            break

     # Trouver l'index du 1er caractère de l'alphabet dans la ligne en partant de la fin

    nEnd = len(sLine)
    for i in range(len(sLine) - 1, -1, -1):
        if sLine[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàéiôèuÀÉIÖÜàéiôèu":
            nEnd = i
            break

    return nStart, nEnd

def main():
    # Chemins des fichiers
    file1_path = "umi1_1.txt"
    file2_path = "umi1_1.en.fr.txt"
    output_file_path = "umi_trad.txt"

    # Lire les fichiers
    with open(file1_path, "r", encoding="utf-8") as file1, open(file2_path, "r", encoding="utf-8") as file2, open(output_file_path, "w", encoding="utf-8") as output_file:
        # Lire les lignes des fichiers
        lines_file1 = file1.readlines()
        lines_file2 = file2.readlines()

        # boucler sur chaque lignes
        i = 0
        for line1, line2 in zip(lines_file1, lines_file2):
            nIDStart1, nIDEnd1 = fFoundCharID(line1)
            nIDStart2, nIDEnd2 = fFoundCharID(line2)

            sFinal = line1[:nIDStart1] + line2[nIDStart2:nIDEnd2+1] + line1[nIDEnd1+1:]
            
            print(line1)
            print(line2)
            print(sFinal)

            output_file.write(sFinal)

if __name__ == "__main__":
    main()