#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int x, cost;

    Edge(int x_,int cost_){
        x = x_; 
        cost = cost_;
    }
};
// 출발, 도착
int s,e;

struct Rem{
    int remain;
    int floor;

    Rem(int remain_, int floor_) : remain(remain_), floor(floor_) {}
}; 

Rem remainArr[10000]; // 1~10000까지 remain

void calRemain (){
    int v = 1;
    int floor = 1;
    for (int i = 1; i <= 10000; i++){
        int remain = (i - v);
        remainArr[i-1] = Rem(remain, floor);

        if (remain == 0){
            floor++;
            v += floor;
        }
    }
}

// 인접 리스트 반환
vector<int> adj (int x){
    vector<int> adjList;
    int floor = remainArr[x-1].floor;
    int under_right_x = x+floor;
    int under_left_x = under_right_x+1;
    if (under_right_x <= 10000)
        adjList.push_back(under_right_x);
    if (under_left_x <= 10000)
        adjList.push_back(under_left_x);
    
    if (x == 1){
        return adjList;
    }
    // 마지막인 경우 -> 최적화 
    int right_x = x-1;
    int left_x = x+1;
    int up_right_x = x-floor;
    int up_left_x = up_right_x+1;
    if (remainArr[x-1].remain != 1){
        adjList.push_back(up_right_x);
        adjList.push_back(right_x);
    }else if(remainArr[x-1].remain != 0){
        adjList.push_back(up_left_x);
        adjList.push_back(left_x);
    }
    return adjList;
}



// bfs 계산
int bfs(int start){
    queue<Edge> q;
    q.push(Edge(start, 0));

    int visited[10000] = {false, };

    while(!q.empty()){
        Edge curr = q.front();
        q.pop();

        if (visited[curr.x]) 
            continue;
        visited[curr.x] = true;

        // 종료
        if (curr.x == e) 
            return curr.cost;

        vector<int> adjList = adj(curr.x);
        for (int i = 0; i < adjList.size(); i++){
            q.push(Edge(adjList[i], curr.cost+1));
        }
        
        return 0;
        

    }
}

int main(){
    int t;
    cin >> t;
    calRemain();
    for (int i = 0; i < 10; i++){
        cout << remainArr[i].remain << remainArr[i].floor;
    }
    for (int i = 0; i < t; i++){

        cin >> s >> e;
        
        int cost = bfs(s);

        cout << cost;

    }
    return 0;
}