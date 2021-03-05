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
            result=0; //FUNCAO FALTANTE VAI AQUI
            cout << "O resultado e: " << result;
            condicao = 0;
        } else if (opcao == 2){
            cout << "\nDIGITE O SEU NUMERO:";
            cin >> n;
            result = convertBinToDec(n);
            cout << "O resultado e: " << result;
            condicao = 0;

        } else { condicao = 0 } //se digitou outra opcao





    } while(condicao == 1);


    return 0;
}

int convertBinToDec(long long n)
{
    int dec = 0, i = 0, resto;
    while (n!=0)
    {
        resto = n%10;
        n /= 10;
        dec += resto*pow(2,i);
        ++i;
    }
    return dec;

}

