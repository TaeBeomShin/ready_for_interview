<h1>인터뷰 질문 및 답변 정리</h1>

<h2>자료구조</h2>
<details markdown="1">
<summary>배열과 링크드리스트의 차이점에 대해서 설명해 주세요.</summary>
배열과 링크드리스트의 차이점은 자료의 저장방식과 그로 인한 시간복잡도 차이입니다.
배열은 테이블에 값을 저장하는 구조를 가지고 있습니다. 링크드 리스트는 값과 이전 자료와 이후 자료의 주소값을 저장하는 구조를 가지고 있습니다.
그래서 배열의 경우에는 자료의 인덱스를 알 경우 O(1)만에 탐색이가 가능하나 삭제와 삽입에 있어서 값을 옮겨줘야 하기 떄문에 O(n)만큼걸립니다.
링크드리스트의 경우에는 위치를 따로 저장하지 않기 떄문에 탐색에 O(N)만큼 걸리지만 삭제와 삽입이 O(1)만에 됩니다.
탐색이 자주 일어나거나 메모리 공간의 낭비가 없을 경우에는 배열, 삽입/삭제가 자주 일어나는 경우 링크드 리스트를 사용합니다.
</details>
<details markdown="1">
<summary>왜 링크드 리스트를 사용하나요?</summary>
링크드 리스트가 배열에 비해서 삽입과 삭제에 있어서 시간복잡도가 낮고, 낭비되는 메모리 공간이 적기때문에 사용합니다.
</details>
<details markdown="1">
<summary>Array vs ArrayList vs LinkedList를 간단히 비교해주세요</summary>
Array의 경우에는 인덱스를 알경우 자료의 탐색에 이점이 있고, ArrayList의 경우 탐색과 array보다 좀 더
유연하게 메모리 공간을 사용할수 있다는 장점이 있습니다. LinkedList는 삽입과 삭제를 O(1)만에 처리할 수 있다는 이점이 있습니다.

[세 자료구조 비교](https://velog.io/@adam2/Array%EC%99%80-List%EA%B7%B8%EB%A6%AC%EA%B3%A0-Java-List#:~:text=%ED%95%98%EB%8A%94%20%EA%B2%83%EC%9D%B4%20%EC%A2%8B%EB%8B%A4.-,%EB%B0%B0%EC%97%B4%EA%B3%BC%20ArrayList%EC%9D%98%20%EC%B0%A8%EC%9D%B4,element%EB%A7%8C%20%EB%8B%B4%EC%9D%84%20%EC%88%98%20%EC%9E%88%EB%8B%A4.)
</details>
<details markdown="1">
<summary>스택과 큐에 대해서 설명해 주세요.</summary>
스택은 LIFO 즉, 후입선출의 특성을 갖는 자료구조입니다. 큐는 FIFO 즉, 선입선출의 특성을 갖는 자료구조입니다. 스택의 경우 함수의 콜스택, 문자열의 역순 출력, 연산자 후위 표기법 등에서 사용됩니다.
큐의 경우 버퍼나 BFS 등에 사용됩니다.

</details>
<details markdown="1">
<summary>스택과 큐는 어떤 경우에 사용될까요? 예를 들어 설명해보세요</summary>
스택의 경우 함수의 콜스택, 문자열의 역순 출력, 연산자 후위 표기법 등에서 사용됩니다.
큐의 경우 버퍼나 BFS 등에 사용됩니다.

</details>
<details markdown="1">
<summary>해시 테이블에 대해서 설명해 주세요.</summary>
해시 테이블은 키와 값형태로 자료를 저장하는 테이블입니다. 충돌이 발생하지 않을경우 평균적으로 O(1)만에 자료를 탐색할 수 있다는 장점을 가집니다. 해시 테이블은 각각의 key값에 해시함수를 적용해 배열의 고유한 index를 저장하고 index를 활용해 값을 저장하거나 검색합니다.

[해쉬테이블 총정리](https://mangkyu.tistory.com/102)

꼬리질문
- 자바를 사용할 경우, HashTable과 HashMap의 차이는 무엇인가요?
</details>
<details markdown="1">
<summary>대표적인 해쉬함수로는 어떤 것이 있나요?</summary>
대표적인 해쉬 함수로는 입력값을 테이블의 크기로 나눈 나머지를 통한 division method, 각 key의 문자열을 아스키 코드로 바뀌고 합한 데이터를 주소로 사용하는 Digit Folding, 숫자로 된 key값 k와 0과 1사이의 실수 A, 2의 제곱수인 mdㄹ 사용한 Mutiplication Method가 있습니다.

</details>
<details markdown="1">
<summary>해시에서 충돌이 일어나는 경우 어떻게 해결할 수 있나요?</summary>
해쉬에서 충돌이 일어나는 경우, 분리 연결법과 개방 주소법 크게 두가지로 해결할 수 있습니다.
분리 연결법은 연결리스트로 새로운 노드를 추가해서 다음 데이터의 주소를 저장하는 방법입니다.
개방 주소법은 해쉬 함수로 얻은 주소가 아닌 다른 주소에 데이터를 주소하도록 허용하는 방법입니다.
추가적으로 개방주소법에 충돌이 일어날 경우 일정 수 만큼 더해서 주소 값을 변경하는 선형 탐사와, 제곱 탐사도 있습니다.
</details>
<details markdown="1">
<summary>트리의 순회 방식 4가지에 대해 설명해보세요. </summary>
트리의 순회방식에는 전위 순회, 중위 순회, 후위 순회, 레벨 순회가 있습니다. 전위 순회는 부모, 왼쪽자식, 오른쪽 자식 순서로 방문합니다. 중위 순회는 왼쪽자식 부모 오른쪽 자식 순서로 방문합니다.
후위 순회는 왼쪽 자식, 부모, 오른쪽 자식 순서로 방문합니다. 레벨 순회는 BFS처럼 동작합니다. 깊이가 동일한 노드부터 방문합니다.

[4가지 순회방법](https://m.blog.naver.com/ohj3423/222360973104)
</details>
<details markdown="1">
<summary>포화(Perfect) 이진트리, 완전(Complete) 이진트리, 정(Full) 이진트리의 차이점에 대해 각각 설명해주세요.</summary>
포화 이진 트리는 리프가 아닌 자식들은 모두 2개의 자식을 가지는 트리입니다. 완전 이진 트리는 포화 이진 트리의 리프를 오른쪽에서 부터 제거해서 얻어질 수 있는 이진 트리입니다. 정 이진트리는 모든 노드가 0개 또는 2개의 자식만을 가지는 이진트리입니다.
</details>
<details markdown="1">
<summary>그래프와 트리의 차이점에 대해서 설명해 주세요.</summary>
트리는 그래프에 포함되며, 둘의 차이는 트리에서는 사이클을 허용하지 않는다는 것입니다.
</details>
<details markdown="1">
<summary>힙 자료구조에 대해 설명해 주세요.</summary>
힙 자료구조는 완전 이진트리의 일종으로 최대힙과 최소힙으로 나누어 집니다.
최소힙은 부모노드보다 자식노드가 항상 큰 이진트리이고, 최대힙은 부모노드보다 자식노드가 항상 작은 이진트리 입니다.
</details>
<details markdown="1">
<summary>힙의 삽입과 삭제는 어떻게 이루어지나요?</summary>
힙의 삽입은 새로운 원소가 들어오면 일단 새로운 노드를 힙의 마지막 노드에 삽입합니다.
삽입을 한뒤 힙의 조건에 따라 부모노드와 비교하고 맞지 않으면 위치를 바꿔주는 과정을 반복합니다.
합의 삭제는 루트 노드를 삭제한 다음 마지막 노드를 루트노드에 가져오고 마찬가지로, 힙의 조건을 만족하는지 체크하며 자식노드와 위치를 바뀌는 과정을 반복합니다. 이때 두 자식노드중 최대힙의 경우 더 큰 자식을 위로 보냅니다.

[heap 삽입 삭제 과정](https://makemethink.tistory.com/136)
</details>
<details markdown="1">
<summary>Heapify할 때 걸리는 시간?</summary>


[heapify 시간복잡도](https://velog.io/@emplam27/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%ED%9E%99Heap#%ED%9E%99%EC%9D%B4-%EC%95%84%EB%8B%8C-%EB%B0%B0%EC%97%B4%EC%9D%84-%ED%9E%99%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0build-heap)
[heapify](https://chayan-memorias.tistory.com/116)
</details>

<details markdown="1">
<summary>Heap vs Tree 어느 경우에 어떤 것을 사용하는 것이 좋을지</summary>
최댓값 및 최솟값을 찾아내는 연산이 필요할 때 사용합니다. 구체적으로 다익스트라 알고리즘에서 최소 비용의
간선을 찾을때 heap자료구조를 이용합니다.
Tree는 여러 개체들 사이의 계층구조를 표현해야할 때 주로 사용합니다.

[Tree](https://makemethink.tistory.com/125)
</details>

<details markdown="1">
<summary>배열 → HeapSort하는 과정 설명</summary>
배열의 원소 n개를 heapify 해주는 과정이기 때문에 O(nlogn)의 시간복잡도를 가집니다.
</details>

<details markdown="1">
<summary>Trie에 대해 설명, 어떤 경우에 사용하는지</summary>
트라이란 주로 문자열의 집합을 표현하는데 사용되는 자료구조입니다.
트라이의 한 노드를 표현하는 객체는 자손노드들을 가리키는 포인터 목록과 종료 노드인지 나타내는
불리언 값으로 구성되어있습니다. 문자열 중 겹치는 부분을 하나의 경로에 같이 저장합니다.
</details>

<details markdown="1">
<summary>최소 신장 트리에 대해서 설명해 주세요.</summary>
최소 신장트리는 그래프에서 그래프의 모든 정점을 포함하는 트리입니다. 최소 신장트리를 구하는 알고리즘에는
정점 선택 기반의 프림 알고리즘과 간선 선택 기반의 크루스칼 알고리즘이 있습니다.
</details>
