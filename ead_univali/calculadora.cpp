#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<string.h>


using namespace std;

int bindec(int num)   
{
       int i, tam, acumula = 0;
       tam = strlen(num); //verifica quantos digitos tem no num
       
       //le os digitos da direita para esquerda
       for (i = tam-1; i >= 0; i--){
            //quando bin=1, calcula a cada vez a potencia do 2
            if(num[i] == '1'){
                acumula += pow(2, tam-1-i) 
            }
       }
       
       return acumula;
 }

int decbin(int num)    
{
   //conversao de num
}

int main()
{
    char num[8];
    int result;
        
    cout << "Calculadora de Conversão de Bases";
    cout << "Digite a conversão desejada:\n[1] - binário para decimal \n[2] - decimal para binário";

    cin >> num;
    
    if(num1 == 1) {
    
    	result = bindec(num);	
    		
    } else {
    	result = decbin(num);
    }
    
    cout << "O resultado da conversão foi: " << result;
    
    return 0;
  
}
