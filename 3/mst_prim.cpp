#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <fstream>




class UWGraph{
public:

    std::vector<std::vector<std::pair<int, int>>> adj_list;
    int size;


    UWGraph(int n){
        adj_list.resize(n);
        size = n;
    }


    void add_edge(int i, int j, int w){
        adj_list[i].push_back(std::make_pair(j, w));
        adj_list[j].push_back(std::make_pair(i, w));
    }

    void print(){
        for (int i = 0; i < size; i++)
            for (auto x : adj_list[i])
                if (i < x.first)
                    std::cout << i << " - " << x.first << ' ' << x.second << '\n';
    }
};


UWGraph mst_prim(UWGraph g){
    UWGraph mst(g.size);

    auto cmp = [](const std::pair<int,int> a, const std::pair<int,int> b){
                  return (a.second == b.second) ? a.first < b.first : a.second < b.second;};
    
    std::vector<int> min_dist(g.size, INT32_MAX);
    std::vector<int> previous(g.size, -1);
    std::set<std::pair<int,int>, decltype(cmp)> border(cmp);
    
    for (int i = 0; i < g.size; i++){
        if (previous[i] > -1)
            continue;

        border.insert(std::make_pair(i, 0));
        previous[i] = i;
        min_dist[i] = 0;
        
        while (not border.empty()){
            int v = border.begin()->first;
            int w = border.begin()->second;
            border.erase(border.begin());
            mst.add_edge(v, previous[v], w);
            min_dist[v] = 0;

            for (auto e : g.adj_list[v]){
                int u = e.first;
                int wu = e.second;

                if (wu < min_dist[u]){
                    border.erase(std::make_pair(u, min_dist[u]));
                    min_dist[u] = wu;
                    previous[u] = v;
                    auto tmp = border.insert(std::make_pair(u, min_dist[u]));
                }
            }
        }
    }
    return mst;
}




using namespace std;


int main(){
    // auto g = UWGraph(4);

    // g.add_edge(0, 1, 8);
    // g.add_edge(0, 3, 3);
    // g.add_edge(1, 2, 2);
    // g.add_edge(1, 3, 5);
    // g.add_edge(2, 3, 6);

    // g.print();
    // cout << "##########\n";

    // //      (0)
    // //     /   \
    // //    3     8
    // //   /       \
    // // (3)---5---(1) 
    // //   \       /
    // //    6     2
    // //     \   /
    // //      (2)

    // auto t = mst_prim(g);
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

    auto t = mst_prim(g);
    auto cmp = [](const pair<int, int> a, const pair<int, int> b){ return a.first < b.first; };

    ofstream output("./_output_prim.txt");
    for (int i = 0; i < g.size; i++){
        sort(t.adj_list[i].begin(), t.adj_list[i].end(), cmp);
        for (auto x : t.adj_list[i])
            if (x.first > i)
                output << i << " - " << x.first << " " << x.second << '\n';
    }
    output.close();
}