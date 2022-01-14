import csv

def tti():
    number_of_childrens=0
    two_meter_tall=0
    tti_indexes=[]
    heightest_children=[]
    average_tall=0
    index_cat1=0
    index_cat2=0
    index_cat3=0
    index_cat4=0
    with open("tti.txt","r",encoding='utf-8') as file:
        txt_file=csv.reader(file,delimiter='\t')
        for index,i in enumerate(txt_file):
            if index ==0:
                continue
            else:
                number_of_childrens+=1
                if (int(i[1])>200):
                    two_meter_tall+=1
                if len(heightest_children)==0:
                    heightest_children=[i]
                elif int(i[2])>int(heightest_children[0][2]):
                    heightest_children.append(i)
                    heightest_children.pop(0)
                average_tall+=(int(i[1])/100)
                height=int(i[2])
                tall=int(i[1])/100
                tti_index=height/(tall**2)
                tti_index=("%.2f" % tti_index)
                if float(tti_index)>30:
                    index_cat1+=1
                elif 30>float(tti_index)>25:
                    index_cat2+=1
                elif 25>float(tti_index)>18:
                    index_cat3+=1
                else:
                    index_cat4+=1
                children=[i[0],str(tti_index)]
                tti_indexes.append(children)
        print(f"A diákok száma: {number_of_childrens}")
        print(f"{two_meter_tall} diák magasabb, mint 2 méter.")
        print("A diákok átlagos magassága "+("%.2f" % (average_tall/number_of_childrens))+" méter.")
        print(f"{heightest_children[0][0]} a leg túlsúlyosabb {heightest_children[0][2]} kilóval.")
    with open("index.txt","w",newline='',encoding='utf-8') as file:
        main_index_cat=[["30 és felette: ",index_cat1],["25-30: ",index_cat2],["18-25: ",index_cat3],["18 alatt: ",index_cat4]]
        header=["Név","TTI-Index"]
        txt_file=csv.writer(file,delimiter='\t')
        txt_file.writerow(header)
        txt_file.writerows(tti_indexes)
        txt_file.writerows(main_index_cat)
        
        
tti()