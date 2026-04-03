class MyHashSet {
private:
    vector<int> data = vector<int>(1000002, 0);
public:
    MyHashSet() {
        
    }
    
    void add(int key) {
        if(data[key] == 0){
            data[key] = 1;
        }
    }
    
    void remove(int key) {
        if(data[key] != 0){
            data[key] = 0;
        }
    }
    
    bool contains(int key) {
        bool ans = false;
        if(data[key] == 1){
            ans = true;
        }
        return ans;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */