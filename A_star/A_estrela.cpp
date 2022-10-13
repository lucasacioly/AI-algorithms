#include <iostream>
#include <utility>
#include <vector>
#include <queue>
using namespace std;


class Distances{
public:
    vector < vector < float > > DistanciasDiretas; // matriz de distâncias diretas
    vector < vector < float > > DistanciasReais; // matriz com as distâncias reais
    Distances(){
        DistanciasDiretas.resize(15);
        DistanciasReais.resize(15);
        for(int i = 0; i < 15; i++){
            DistanciasDiretas[i].resize(15);
            DistanciasReais[i].resize(15);
        }
        DistanciasDiretas[1][1] = 0;
        DistanciasDiretas[1][2] = 10;
        DistanciasDiretas[1][3] = 18.5;
        DistanciasDiretas[1][4] = 24.8;
        DistanciasDiretas[1][5] = 36.4;
        DistanciasDiretas[1][6] = 38.8;
        DistanciasDiretas[1][7] = 35.8;
        DistanciasDiretas[1][8] = 25.4;
        DistanciasDiretas[1][9] = 17.6;
        DistanciasDiretas[1][10] = 9.1;
        DistanciasDiretas[1][11] = 16.7;
        DistanciasDiretas[1][12] = 27.3;
        DistanciasDiretas[1][13] = 27.6;
        DistanciasDiretas[1][14] = 29.8;

        DistanciasDiretas[2][2] = 0;
        DistanciasDiretas[2][3] = 8.5;
        DistanciasDiretas[2][4] = 14.8;
        DistanciasDiretas[2][5] = 26.6;
        DistanciasDiretas[2][6] = 29.1;
        DistanciasDiretas[2][7] = 26.1;
        DistanciasDiretas[2][8] = 17.3;
        DistanciasDiretas[2][9] = 10;
        DistanciasDiretas[2][10] = 3.5;
        DistanciasDiretas[2][11] = 15.5;
        DistanciasDiretas[2][12] = 20.9;
        DistanciasDiretas[2][13] = 19.1;
        DistanciasDiretas[2][14] = 21.8;

        DistanciasDiretas[3][3] = 0;
        DistanciasDiretas[3][4] = 6.3;
        DistanciasDiretas[3][5] = 18.2;
        DistanciasDiretas[3][6] = 20.6;
        DistanciasDiretas[3][7] = 17.6;
        DistanciasDiretas[3][8] = 13.6;
        DistanciasDiretas[3][9] = 9.4;
        DistanciasDiretas[3][10] = 10.3;
        DistanciasDiretas[3][11] = 19.5;
        DistanciasDiretas[3][12] = 19.1;
        DistanciasDiretas[3][13] = 12.1;
        DistanciasDiretas[3][14] = 16.6;

        DistanciasDiretas[4][4] = 0;
        DistanciasDiretas[4][5] = 12;
        DistanciasDiretas[4][6] = 14.4;
        DistanciasDiretas[4][7] = 11.5;
        DistanciasDiretas[4][8] = 12.4;
        DistanciasDiretas[4][9] = 12.6;
        DistanciasDiretas[4][10] = 16.7;
        DistanciasDiretas[4][11] = 23.6;
        DistanciasDiretas[4][12] = 18.6;
        DistanciasDiretas[4][13] = 10.6;
        DistanciasDiretas[4][14] = 15.4;

        DistanciasDiretas[5][5] = 0;
        DistanciasDiretas[5][6] = 3;
        DistanciasDiretas[5][7] = 2.4;
        DistanciasDiretas[5][8] = 19.4;
        DistanciasDiretas[5][9] = 23.3;
        DistanciasDiretas[5][10] = 28.2;
        DistanciasDiretas[5][11] = 34.2;
        DistanciasDiretas[5][12] = 24.8;
        DistanciasDiretas[5][13] = 14.5;
        DistanciasDiretas[5][14] = 17.9;

        DistanciasDiretas[6][6] = 0;
        DistanciasDiretas[6][7] = 3.3;
        DistanciasDiretas[6][8] = 22.3;
        DistanciasDiretas[6][9] = 25.7;
        DistanciasDiretas[6][10] = 30.3;
        DistanciasDiretas[6][11] = 36.7;
        DistanciasDiretas[6][12] = 27.6;
        DistanciasDiretas[6][13] = 15.2;
        DistanciasDiretas[6][14] = 18.2;

        DistanciasDiretas[7][7] = 0;
        DistanciasDiretas[7][8] = 20;
        DistanciasDiretas[7][9] = 23;
        DistanciasDiretas[7][10] = 27.3;
        DistanciasDiretas[7][11] = 34.2;
        DistanciasDiretas[7][12] = 25.7;
        DistanciasDiretas[7][13] = 12.4;
        DistanciasDiretas[7][14] = 15.6;

        DistanciasDiretas[8][8] = 0;
        DistanciasDiretas[8][9] = 8.2;
        DistanciasDiretas[8][10] = 20.3;
        DistanciasDiretas[8][11] = 16.1;
        DistanciasDiretas[8][12] = 6.4;
        DistanciasDiretas[8][13] = 22.7;
        DistanciasDiretas[8][14] = 27.6;


        DistanciasDiretas[9][9] = 0;
        DistanciasDiretas[9][10] = 13.5;
        DistanciasDiretas[9][11] = 11.2;
        DistanciasDiretas[9][12] = 10.9;
        DistanciasDiretas[9][13] = 21.2;
        DistanciasDiretas[9][14] = 26.6;


        DistanciasDiretas[10][10] = 0;
        DistanciasDiretas[10][11] = 17.6;
        DistanciasDiretas[10][12] = 24.2;
        DistanciasDiretas[10][13] = 18.7;
        DistanciasDiretas[10][14] = 21.2;

        DistanciasDiretas[11][11] = 0;
        DistanciasDiretas[11][12] = 14.2;
        DistanciasDiretas[11][13] = 31.5;
        DistanciasDiretas[11][14] = 35.5;

        DistanciasDiretas[12][12] = 0;
        DistanciasDiretas[12][13] = 28.8;
        DistanciasDiretas[12][14] = 33.6;

        DistanciasDiretas[13][13] = 0;
        DistanciasDiretas[13][14] = 5.1;

        DistanciasDiretas[14][14] = 0;

        for(int i = 1; i < 15; i++){
            for(int j = 1; j < 15; j++){
                DistanciasDiretas[i][j] *= 2;
            }
        }

        DistanciasReais[1][2] = 20;
        DistanciasReais[2][3] = 17;
        DistanciasReais[3][4] = 12.6;
        DistanciasReais[4][5] = 26;
        DistanciasReais[5][6] = 6;
        DistanciasReais[5][7] = 4.8;
        DistanciasReais[5][8] = 60;
        DistanciasReais[4][8] = 30.6;
        DistanciasReais[3][9] = 18.8;
        DistanciasReais[2][9] = 20;
        DistanciasReais[2][10] = 7;
        DistanciasReais[8][9] = 19.2;
        DistanciasReais[9][11] = 24.2;
        DistanciasReais[8][12] = 12.8;
        DistanciasReais[3][13] = 37.4;
        DistanciasReais[4][13] = 25.6;
        DistanciasReais[13][14] = 10.2;
    }

};

class MatrizAdj{ // mapear as estações que possuem mais de uma linha
public:
    vector < pair < pair < int, string >, vector < int > > > matrizDeAdj;
    MatrizAdj(){
        matrizDeAdj.push_back({{2,"azul"}, {1,3}});
        matrizDeAdj.push_back({{2,"amarelo"}, {9,10}});
        matrizDeAdj.push_back({{3,"azul"}, {4,2}});
        matrizDeAdj.push_back({{3,"vermelho"}, {9,13}});
        matrizDeAdj.push_back({{4,"azul"}, {3,5}});
        matrizDeAdj.push_back({{4,"verde"}, {8,13}});
        matrizDeAdj.push_back({{5,"azul"}, {6,4}});
        matrizDeAdj.push_back({{5,"amarelo"}, {7,8}});
        matrizDeAdj.push_back({{8,"amarelo"}, {9,5}});
        matrizDeAdj.push_back({{8,"verde"}, {12,4}});
        matrizDeAdj.push_back({{9,"amarelo"}, {8,2}});
        matrizDeAdj.push_back({{9,"vermelho"}, {11,3}});
        matrizDeAdj.push_back({{13,"verde"}, {14,4}});
        matrizDeAdj.push_back({{13,"vermelho"}, {3}});
    }
};

class Node{ // objeto que será inserido na fronteira
    Distances distancias;
public:
    Node* noPai;
    int noFinal;
    string estacaoAtual;
    int id;
    float h;
    float g;
    float f; //parâmetro de comparação na priority queue

    Node(int idNode, Node* pai, int final, string estacao){
        noPai = pai;
        noFinal = final;
        id = idNode;
        estacaoAtual = std::move(estacao);

        if (noPai != nullptr){
            if(id < noPai->id){
                g = noPai->g + distancias.DistanciasReais[id][noPai->id];
            }
            else{
                g = noPai->g + distancias.DistanciasReais[noPai->id][id];
            }
        }
        else{
            g = 0;
        }

        if(id < noFinal){
            h = distancias.DistanciasDiretas[id][noFinal];
        }
        else{
            h = distancias.DistanciasDiretas[noFinal][id];
        }

        f = g + h;
    }
};

class Compare{
public:
    bool operator()(const Node* a, const Node* b){
        return a->f > b->f;
    }
};

void printarCaminho(Node* noAtual){
    if(noAtual->noPai != nullptr){
        printarCaminho(noAtual->noPai);
    }
    else{
        cout << "------------ RESULTADO --------------\n";
    }
    cout << "Estacao: " << noAtual->id
        << " | Linha: " << noAtual->estacaoAtual
        << " | Custo total = " << noAtual->g << "\n";
}

void A_estrela(int Final, Node* Inicial){
    priority_queue < Node* , vector < Node* >, Compare> fronteira;
    fronteira.push(Inicial);
    string linhaAtual;
    Distances distancias;
    MatrizAdj matrizDeAdj;
    bool continuar;
    while(!fronteira.empty()) {

        // printa fronteira
        priority_queue<Node *, vector<struct Node *>, Compare> copia_fronteira = fronteira;
        cout << "------------------ Fronteira -------------------\n";
        while (!copia_fronteira.empty()){
            cout << "Estacao: " << copia_fronteira.top()->id
                 << " Linha: " << copia_fronteira.top()->estacaoAtual
                 << " f = " << copia_fronteira.top()->f <<"\n";

            copia_fronteira.pop();
        }
        cout << "--------------------------------------------------\n" ;

        //Selecionar o primeiro nó (estado) da fronteira
        Node* topoFronteira = fronteira.top();
        fronteira.pop();

        //Testar se o nó selecionado é um estado final (objetivo)
        if (topoFronteira->id == Final) {
            printarCaminho(topoFronteira);
            return;
        }

        //Gerar um novo conjunto de estados aplicando ações ao estado selecionado e inserir na fronteira
        if (topoFronteira->id == 2 || topoFronteira->id == 3 || topoFronteira->id == 4 || topoFronteira->id == 5 ||
            topoFronteira->id == 8 || topoFronteira->id == 9 || topoFronteira->id == 13) {
            linhaAtual = topoFronteira->estacaoAtual;
        } else {
            linhaAtual = ""; // nesse caso só há uma linha possível para a estação atual
        }

        for (int i = 1; i < 15; i++) { // varre linha e colunas da matriz de distâncias reais em busca das estações atingíveis a partir da estação atual
            if (distancias.DistanciasReais[topoFronteira->id][i] != 0 ||
                distancias.DistanciasReais[i][topoFronteira->id] != 0) {
                // caso de só haver uma possível linha na estação atual
                if (linhaAtual.empty() && (topoFronteira->noPai == nullptr || (topoFronteira->noPai != nullptr && topoFronteira->noPai->id != i))) {
                    Node* novo = new Node(i, topoFronteira, Final, topoFronteira->estacaoAtual);
                    fronteira.push(novo);
                }
                // caso de haver mais de uma linha na estação atual
                else {
                    continuar = true;
                    for (int j = 0; j < 14; j++) {
                        if (matrizDeAdj.matrizDeAdj[j].first.first == topoFronteira->id) {
                            for (int k = 0; k < matrizDeAdj.matrizDeAdj[j].second.size(); k++) {
                                if (matrizDeAdj.matrizDeAdj[j].second[k] == i){
                                    continuar = false;
                                    if(matrizDeAdj.matrizDeAdj[j].first.second == linhaAtual && (topoFronteira->noPai == nullptr || (topoFronteira->noPai != nullptr && topoFronteira->noPai->id != i))) {
                                        Node* novo = new Node(i, topoFronteira, Final, topoFronteira->estacaoAtual);
                                        fronteira.push(novo);
                                        break;
                                    }
                                }
                            }
                            if(!continuar){
                                break;
                            }
                        }
                    }


                }
            }
        }
        // se a estação possui uma segunda linha além da atual, troca de linha e coloca na fronteira
        if ((topoFronteira->noPai != nullptr && topoFronteira->noPai->id != topoFronteira->id) || topoFronteira->noPai == nullptr){
            string estacao_mudada;
            bool entrou = false;
            switch (topoFronteira->id) {
                case 2:
                    if (topoFronteira->estacaoAtual == "azul") { estacao_mudada = "amarelo"; }
                    else { estacao_mudada = "azul"; }
                    entrou = true;
                    break;
                case 3:
                    if (topoFronteira->estacaoAtual == "azul") { estacao_mudada = "vermelho"; }
                    else { estacao_mudada = "azul"; }
                    entrou = true;
                    break;
                case 4:
                    if (topoFronteira->estacaoAtual == "azul") { estacao_mudada = "verde"; }
                    else { estacao_mudada = "azul"; }
                    entrou = true;
                    break;
                case 5:
                    if (topoFronteira->estacaoAtual == "azul") { estacao_mudada = "amarelo"; }
                    else { estacao_mudada = "azul"; }
                    entrou = true;
                    break;
                case 8:
                    if (topoFronteira->estacaoAtual == "verde") { estacao_mudada = "amarelo"; }
                    else { estacao_mudada = "verde";}
                    entrou = true;
                    break;
                case 9:
                    if (topoFronteira->estacaoAtual == "vermelho") { estacao_mudada = "amarelo"; }
                    else { estacao_mudada = "vermelho"; }
                    entrou = true;
                    break;
                case 13:
                    if (topoFronteira->estacaoAtual == "verde") { estacao_mudada = "vermelho"; }
                    else { estacao_mudada = "verde"; }
                    entrou = true;
                    break;
            }
            if (entrou){
                Node* mudancaEstacao = new Node(topoFronteira->id, topoFronteira, Final, estacao_mudada);
                mudancaEstacao->g += 4;
                mudancaEstacao->f += 4;
                fronteira.push(mudancaEstacao);

            }
        }

    }
}

int main(){

    MatrizAdj tabelaDeAdj;
    Distances tabelaDistancias;
    int idInicial;
    int idFinal;
    string linhaInicial;

    printf("Digite a estacao inicial: ");
    cin >> idInicial;
    printf("\nDigite a linha inicial: ");
    cin >> linhaInicial;
    printf("\nDigite a estacao final: ");
    cin >> idFinal;
    Node inicial(idInicial, nullptr, idFinal, linhaInicial);
    A_estrela(idFinal, &inicial);

    return 0;
}