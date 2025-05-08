from multiprocessing import Manager

class fastaReader():
    def __init__(self):
        self.path = "C:\\Users\\gusco\\Desktop\\6to Semestre\\Análisis y Modelación de Sistemas\\parall_BFOA-main\\multifasta.fasta"
        
        self.seqs = list()
        self.names = list()
        self.read()

    def read(self):
        f = open(self.path, "r")
        lines = f.readlines()
        f.close()
        seq = ""
        for line in lines:
            if line[0] == ">":
                self.names.append(line[1:].strip())
                if seq != "":
                    self.seqs.append(seq)
                seq = ""
            else:
                seq += line.strip()
        self.seqs.append(seq)