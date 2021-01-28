#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>




class DisjointSet{

    int n;
    int *rank, *parent; 


    public:
    DisjointSet(int n){
        this->n = n;
        rank = new int[n]; 
        parent = new int[n];
        for (int i = 0; i < n; i++){
            parent[i] = i;
            rank[i] = 1;
        }
    }
    

    ~DisjointSet(){
        delete rank, parent;
    }


    int find(int x){
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }


    void unite(int x, int y){
        x = find(x);
        y = find(y);
        if (x != y){
            if (rank[x] < rank[y])
                parent[x] = y;
            else if (rank[x] > rank[y])
                parent[y] = x;
            else{
                parent[x] = y;
                rank[x]++;
            }
        }
    }
};




struct UWGEdge{

    int i, j, w;


    UWGEdge(int a, int b, int c){
        i = a;
        j = b;
        w = c;
    }
};


class UWGraph{
public:

    int vertices;
    std::vector<UWGEdge> edge_list;


    UWGraph(int v){
        vertices = v;
    }


    void add_edge(int i, int j, int w){
        edge_list.push_back(UWGEdge(i, j, w));
    }


    void print() const{
        for (auto e : edge_list){
            std::cout << e.i << "  <- " << e.w << " ->  " << e.j << '\n';
        }
        std::cout << '\n';
    }
};




using namespace std;


UWGraph mst_kruskal(UWGraph g){
    
    auto mst = UWGraph(g.vertices);
    auto djset = DisjointSet(g.vertices);

    auto cmp = [](const auto &a, const auto &b){ return a.w < b.w; };
    sort(g.edge_list.begin(), g.edge_list.end(), cmp);
    
    for (auto e : g.edge_list){
        if (djset.find(e.i) != djset.find(e.j)){
            djset.unite(e.i, e.j);
            mst.add_edge(e.i, e.j, e.w);
        }
    }
    return mst;
}


bool cmp_output(const UWGEdge &a, const UWGEdge &b){
    if (a.i == b.i) { return a.j < b.j; }
    else { return a.i < b.i; }
}


int main(){
    // auto g = UWGraph(4);

    // g.add_edge(0, 1, 8);
    // g.add_edge(0, 3, 3);
    // g.add_edge,e(1, 2, 2);
    // g.add_edge(1, 3, 5);
    // g.add_edge(2, 3, 6);

    // // g.print();

    // //      (0)
    // //     /   \
    // //    3     8
    // //   /       \
    // // (3)---5---(1) 
    // //   \       /
    // //    6     2
    // //     \   /
    // //      (2)

    // auto t = mst_kruskal(g);
    // t.print();


    int vertices, edges;
    int i, j ,w;
    ifstream input("./_input.txt");

    input >> vertices >> edges;
    auto g = UWGraph(vertices);

    for (int c = 0; c < edges; c++){
        input >> i >> j >> w;
        g.add_edge(i, j ,w);
    }
    input.close();

    auto t = mst_kruskal(g);

    sort(t.edge_list.begin(), t.edge_list.end(), cmp_output);
    ofstream output("./_output_kruskal.txt");
    for (auto x : t.edge_list){
        output << x.i << " - " << x.j << " " << x.w << '\n';
    }
    output.close();
}



