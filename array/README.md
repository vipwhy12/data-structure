
## Array

<aside>
⚠️ Array는 연관된 data를 메모리상에 연속적이며 순차적으로 미리 할당된 크기 만큼 저장하는 자료구조입니다.

</aside>

- 고정된 저장 공간
- 순차적인 데이터 저장
- Array의 장점은 lookup과 append가 빠르다는 장점을 가지고 있음
- Array의 단점은 fixed-size 특정상 선언시 Array의 크기를 미리 정해야 함.
- Static Memory Allocation
Array의 memory allocation은 compile 단계에서 일어나며 Stack memory 영역에 할당.

### 시간복잡도

|  | Array |
| --- | --- |
| access | $O(1)$ |
| append | $O(1)$ |
| 마지막 원소delete | $O(1)$ |
| insertion | $O(n)$ |
| deletion | $O(n)$ |
| search | $O(n)$ |

---

## Dynamic Array

<aside>
⚠️ Array의 경우 size가 고정되어 있기 때문에 선언시에 설정한 size보다 많은 갯수의 data가 추가되면 저장할 수 없습니다. 이에 반해 Dynamic Array는 저장 공간이 가득차게 되면 resize하여 유동적으로 size를 조절하여 데이터를 저장하는 자료구조이다.

</aside>

- Doubling
Dynamic Array를 resize하는 방법 중 하나 데이터를 추가(append O(1))을 하다가 메모리를 초과하게 되면 기존의 배열 size보다 두배 큰 배열을 선언하고 데이터를 일일이 옮기는 방법이다.
- 분할상환 시간복잡도 Amortized time complexity
Dynamic Array의 append 시간 복잡도는 O(1)일까 O(n)일까?
→ 데이터를  마지막 인덱스에 추가하는 작업은 O(1)작업이 걸린다. 하지만 resize시에는 O(n)으로 발생한다.

분할 상환  분석은 주어진 알고리즘의 시간복잡도나 프로그램을 수행하는데 소요되는 시간 또는 메모리 같은 자원 사용량을 분석하기 위해서 사용하는 기법 중 하나이다. 각각의 연산마다 최악의 경우를 따져본다는 것은 굉장히 어려운 일이기 때문에 분할 상환 분석론이 나오게 되었다. 

Dynamic Array의 append 처럼 자원적 측면에서 상당한 비용을 소모할 수 있는 연산이 있고 같은 연산임에도 고비용을 소모하지 않을 수 있다. 분할상황분석은 알고리즘의 전반적인 연산 집합에 대해 비용이 높은 연산과 덜한 연산 모두를 고려한다. 

따라서 종류의 입력, 입력의 길이, 알고리즘 성능에 영향을 미치는 요인들을 전부 고려하여 한 시퀀스를 수행하는데 필요한 시간의 평균을 구한다.

Dynamic Array 자료구조의 append 시간복잡도는 **amortized** $O(1)$이다.

---

## Linked List

<aside>
⚠️ Linked List는 Node라는 구조체로 이루어져 있다. Node는 데이터 값과 다음 Node의 address를 저장하며, Linked List는 물리적인 메모리상에서는 비연속적으로 저장이 되지만 Linked list를 구성하는 각각의 Node가 next Node의 address를 가리킴으로써 논리적인 연속성을 가진 구조이다.

</aside>

- Dynamic Memory Allocation
Linked List의 경우 runtime 단계에서 새로운 node가 추가될 때마다 memory allocation이 일어나며, Heap 메모리 영역에 할당된다.
- 삽입/삭제가 빈번히 일어날때, 얼마만큼의 데이터를 들어올지 예측할 수 없을 때 사용하면 좋다.

### 시간복잡도

|  | Linked list |
| --- | --- |
| access | $O(n)$ |
| search | $O(n)$ |
| insertion | $O(1)$ |
| deletion | $O(1)$ |