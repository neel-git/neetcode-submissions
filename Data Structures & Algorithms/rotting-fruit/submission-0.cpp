class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        if(n == 0 && m == 0) return 0;
        queue<pair<int,int>> q;
        int total = 0;
        int count = 0;
        int time = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] != 0) total++;
                if(grid[i][j] == 2) {
                    q.push({i,j});
                }
            }
        }

        int dx[4] = {-1,0,1,0};
        int dy[4] = {0,1,0,-1};
        while(!q.empty()){
            int k = q.size();
            count += k;
            while(k--){
                auto it = q.front();
                q.pop();
                for(int i = 0; i < 4; i++){
                    int x = it.first;
                    int y = it.second;

                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(nx < 0 || ny < 0 || nx >= n || ny >= m || grid[nx][ny] != 1) continue;
                    grid[nx][ny] = 2;
                    q.push({nx,ny});
                }
            }
            if(!q.empty()) time++;
        } 

        return count == total ? time : -1;
    }
};
