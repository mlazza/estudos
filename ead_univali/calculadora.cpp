/* CALCULADORA DO PROJETO HANDS ON WORK I
DA UNIVALI - 2021

CONVERSOR DE BASES

autores:
Marlon Lazzarotti
Felipe Navas
*/

#include <iostream>
#include <cmath>

using namespace std;

int convertBinToDec(long long);
int convertDecToBin(int);

int main()
{
    long long n;
    bool condicao = 1;
    int opcao;
    int result;

    do{
        cout << "BEM-VINDO A CALCULADORA CONVERSORA DE BASES";
        cout << "\nESCOLHA A OPÇÃO DESEJADA:";
        cout << "\n[1] - converte decimal em binario";
        cout << "\n[2] - converte binario em decimal";

        cin >> opcao;



        if(opcao == 1){
            cout << "\nDIGITE O SEU NUMERO:";
            cin >> n;
            result = convertDecToBin(n); 
            cout << "O resultado e: " << result << endl;
            condicao = 0;
        } else if (opcao == 2){
            cout << "\nDIGITE O SEU NUMERO:";
            cin >> n;
            result = convertBinToDec(n);
            cout << "O resultado e: " << result << endl;
            condicao = 0;

        } else { condicao = 0; }; //se digitou outra opcao

    } while(condicao == 1);


    return 0;
}

// FUNCAO DE CONVERSAO BINARIO PARA DECIMAL
int convertBinToDec(long long n)
{
    int dec = 0, i = 0, resto;
    while (n !=0 )
    {
        resto = n % 10;
        n /= 10;
        dec += resto * pow(2,i);
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
        //cout << "Passo " << passo++ << ": " << n << "/2, Resto = " << resto << ", quociente = " << n/2 << endl;
        n /= 2;
        binario += resto * i;
        i *= 10;
    }
    return binario;
}