import vim
def emit():
    template = '''// {{{
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <cmath>
#include <cstdio>

using namespace std;

typedef long int i32;
typedef unsigned long int u32;
typedef long long int i64;
typedef unsigned long long int  u64;
typedef pair<i32, i32> PII;
#define IN(x) cin >> x;
#define MEM(a, b) memset(a, (b), sizeof(a))
#define ZERO(a) memset(a, 0, sizeof(a))
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j-1, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.rbegin(), cont.rend()
#define MP make_pair
#define PB push_back
#define PF push_front
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define DEBUG(x) cout << #x << ": " << x << endl;

template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }
// }}}

int main() {
    return 0;
}
'''
    lines = template.split('\n')
    for s in lines:
        vim.current.buffer.append(s)
    vim.current.buffer[:] = vim.current.buffer[-len(lines):]
    vim.command('setlocal foldmethod=marker')
