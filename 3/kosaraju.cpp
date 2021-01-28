#include <vector>
#include <iostream>
#include <stack>
#include <fstream>
#include <algorithm>


using namespace std;


class OrientedGraph{
private:

    vector<vector<int>> adj_list;
    int size;


    void dfs1(int i, vector<bool>& visited, stack<int>& stack_) const{
        visited[i] = true;
        for (int j = 0; j < adj_list[i].size(); j++){
            if (not visited[adj_list[i][j]]){
                dfs1(adj_list[i][j], visited, stack_);
            }
        }
        stack_.push(i);
    }


    void dfs2(int i, vector<bool>& visited, vector<int>& component, OrientedGraph tr) const{
        visited[i] = true;
        component.push_back(i);
        for (auto j : tr.adj_list[i]){
            if (not visited[j]){
                dfs2(j, visited, component, tr);
            }
        }
    }


public:

    OrientedGraph(int n){
        adj_list.resize(n);
        size = n;
    }


    void add_edge(int i, int j){
        adj_list[i].push_back(j);
    }


    OrientedGraph transpose() const{
        OrientedGraph graph(size);
        for (int i = 0; i < size; i++){
            for (auto j = adj_list[i].begin(); j != adj_list[i].end(); j++){
                graph.add_edge(*j, i);
            }
        }
        return graph;
    }


    void kosaraju() const{
        vector<bool> visited(size, false);
        stack<int> stack_;
        
        vector<int> tmp;

        for (int i = 0; i < size; i++){
            if (not visited[i]){
                dfs1(i, visited, stack_);
            }
        }

        fill(visited.begin(), visited.end(), 0);
        auto transposed = transpose();


        while(not stack_.empty()){
            int i = stack_.top();
            stack_.pop();

            vector<int> component;
            if (not visited[i]){
                dfs2(i, visited, component, transposed);
                tmp.push_back(component.size());
            }
        }
        cout << "N of components: " << tmp.size() << "\n\n";
    }


    void print(){
        for (int i = 0; i < size; i++){
            cout << i << ": ";
            for (auto x : adj_list[i]){
                cout << x << ' ';
            } 
            cout << '\n';
        }
        cout << '\n';
    }
};





int main(int argc, char* argv[]){
    auto a = OrientedGraph(9);

    a.add_edge(0, 1);
    a.add_edge(1, 2);
    a.add_edge(2, 0);
    a.add_edge(1, 3);
    a.add_edge(3, 4);
    a.add_edge(4, 3);
    a.add_edge(5, 6);
    a.add_edge(6, 5);
    a.add_edge(5, 7);

    // 0 +---> 1 +---> 3     5 +---> 7
    //                  
    // ^       +       ^     ^
    // |       |       |     |
    // +       |       v     v
    //         |        
    // 2 <-----+       4     6       8

    a.kosaraju();


    auto b = OrientedGraph(8);

    b.add_edge(0, 1);
    b.add_edge(1, 2);
    b.add_edge(2, 3);
    b.add_edge(3, 0);
    b.add_edge(4, 5);
    b.add_edge(5, 6);
    b.add_edge(6, 7);
    b.add_edge(7, 4);
    b.add_edge(0, 4);

    // +---> 3 +---+        +---+ 7 <---+
    // |           |        |           |
    // +           v        v           +
    // 
    // 2           0 <----+ 4           6
    // 
    // ^           +        +           ^
    // |           |        |           |
    // +---+ 1 <---+        +---> 5 +---+

    b.kosaraju();
}