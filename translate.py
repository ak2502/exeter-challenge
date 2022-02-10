import csv
import time
import tracemalloc
import os

tracemalloc.start()
start_time = time.time()

# creating output folder and files
os.mkdir("output")
open("output/performance.txt","x")
open("output/t8.shakespeare.translated.txt","x")
with open('output/frequency.csv', 'wb') as f:
  writer = csv.writer(f)


inputFile = open('t8.shakespeare.txt', 'r').read()

# updating "frequency.csv"
with open('output/frequency.csv','w',newline ='') as dictFreq:
    fieldNames = ['English word','French word','Frequency']
    csvWriter = csv.DictWriter(dictFreq,fieldnames=fieldNames)
    csvWriter.writeheader()

with open('french_dictionary.csv', 'r') as findText:
    readCsv = csv.reader(findText)
    for line in readCsv:
        freq = inputFile.count(line[0])

        with open('output/frequency.csv','a',newline ='') as dictFreq:
            fieldNames = ['English word','French word','Frequency']
            csv_writer = csv.DictWriter(dictFreq,fieldnames=fieldNames)
            csv_writer.writerow({'English word':line[0],'French word':line[1],'Frequency':freq})

        if freq>0:
            inputFile = inputFile.replace(line[0],line[1])

    # updating "t8.shakespeare.translated.txt"
    with open('output/t8.shakespeare.translated.txt','w') as file:
        file.write(inputFile)

# tracking performance
end_time = time.time()
time = round(end_time-start_time)
memory = tracemalloc.get_traced_memory()
memory = memory[1]/(1024*1024)
tracemalloc.stop()

# updating performance.txt
with open('output/performance.txt','w') as per:
    per.write("Time to process: "+str(time//60)+" minutes "+ str(time%60) +" seconds\n")
    per.write("Memory used: "+ str(round(memory,2))+" MB")