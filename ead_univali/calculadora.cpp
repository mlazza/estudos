/* CALCULADORA DO PROJETO HANDS ON WORK I
DA UNIVALI - 2021
CONVERSOR DE BASES
autor:
Marlon Lazzarotti
*/

#include <iostream>
#include <cmath>
#include "math.h"
#include "string.h"

using namespace std;

int convertBinToDec(long long);
int convertDecToBin(int);
int convertHexToDec(char[]);

//PROGRAMA PRINCIPAL
int main()
{
    long long n;
    char hexa_number[] = "";
    bool condicao = 1;
    int opcao;
    int result;

    do
    {
        //MENU DO USUARIO
        cout << "CALCULADORA CONVERSORA DE BASES";
        cout << "\nESCOLHA A OPÇÃO DESEJADA:";
        cout << "\n[1] - converte decimal em binario";
        cout << "\n[2] - converte binario em decimal";
        cout << "\n[3] - converte hexadecimal em decimal";
        cout << "\n[0] - SAIR\n";

        cin >> opcao;

        // opcao decimal para binario
        if (opcao == 1)
        {
            cout << "\nDIGITE O SEU NUMERO:";
            cin >> n;
            result = convertDecToBin(n);
            cout << "O resultado e: " << result << endl;
            condicao = 0;
        }
        // opcao binario para decimal
        else if (opcao == 2)
        {
            cout << "\nDIGITE O SEU NUMERO:";
            cin >> n;
            result = convertBinToDec(n);
            cout << "O resultado e: " << result << endl;
            condicao = 0;
        }
        // opcao hexadecimal para decimal
        else if (opcao == 3)
        {
            cout << "\nDIGITE O SEU NUMERO:";
            cin >> hexa_number;
            result = convertHexToDec(hexa_number);
            cout << "O resultado e: " << result << endl;
            condicao = 0;
        }
        else
        {
            condicao = 0;
        }; //se digitou outra opcao encerra o programa

    } while (condicao == 1);

    return 0;
}

// FUNCAO DE CONVERSAO BINARIO PARA DECIMAL
int convertBinToDec(long long n)
{
    int dec = 0, i = 0, resto;
    while (n != 0)
    {
        resto = n % 10;
        n /= 10;
        dec += resto * pow(2, i);
        ++i;
    }
    return dec;
}

// FUNCAO DE CONVERSAO DECIMAL PARA BINARIO
int convertDecToBin(int n)
{
    long long binario = 0;
    int resto, i = 1, passo = 1;

    while (n != 0)
    {
        resto = n % 2;
        n /= 2;
        binario += resto * i;
        i *= 10;
    }
    return binario;
}

// FUNCAO DE CONVERSAO HEXADECIMAL PARA DECIMAL

int convertHexToDec(char num[]) 
{
   int len = strlen(num);
   int base = 1;
   int temp = 0;
   for (int i=len-1; i>=0; i--) {
      if (num[i]>='0' && num[i]<='9') {
         temp += (num[i] - 48)*base;
         base = base * 16;
      }
      else if (num[i]>='A' && num[i]<='F') {
         temp += (num[i] - 55)*base;
         base = base*16;
      }
   }
   return temp;
}
