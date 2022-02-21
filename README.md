# big-data

This repo presents a way to digest big data corpuses through distributed
systems approaches. The data is stored in an Oracle SQL database and con
sists of several tables regarding warehouse logistics for a company.
The objective of the system is to read historical data from the system
and afterwards output a predicted trend behaviour for several products



## Strategy

To better tackle this problem, we will suppose that our data is given in a non-sql format, so we can focus our efforts in developping our processing methods, rather than focusing on extraction efforts (which are instance-related and can be dealt with later on, regardless of the data processing modules)

The idea is to spread the rigidly structured SQL data into a NoSQL paradigm and then process it using a distributed architecture, possibly using Spark and a Microservices based architecture.




## Project Structure

/  
|[ Root Folder]  
|  
|++README.md   
|  
|--data/  
|------|[Contains corpuses of data to test solutions]  
|------|    
|
|--scripts/  
|---------|[Contains bash scripts to be used on the project]  
|---------|  
|---------|  
|---------|  
|  
|--src/  
|-----|--models/  
|--------------|--open_api/  
|-------------------------|[Contains yml files that define DTOs for the system]  
|-------------------------|  
|-------------------------|++centro_de_distribuicao.yml  
|-------------------------|  
|-------------------------|++compra.yml  
|-------------------------|  
|-------------------------|++estoque.yml  
|-------------------------|  
|-------------------------|++produto.yml  
|-------------------------|  
|-------------------------|++QID.yml  
|-------------------------|  
|-------------------------|++venda.yml  
