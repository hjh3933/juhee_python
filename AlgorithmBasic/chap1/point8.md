### 함수와 클래스

**함수**

- `def 함수명(매개변수):` 형태로 작성한다
- 반복되는 처리를 함수형태로 만들어두고 재사용할 수 있다
- 매개변수: 함수 정의에 사용되는 것, 인수: 실제로 함수에 전달되는 값
- 값에 의한 전달
  - `x = 3`과 같은 변수에 값을 복사하여 `add(x)`와 같은 형태로 값을 전달하는 방식
  - 복사이므로 함수 내에서 값을 변경하여도 실제 변수 x의 값은 변경되지 않는다
- 참조에 의한 전달
  - 변수의 메모리 위치를 전달하는 방법
  - 해당 위치의 값을 바꿔쓰기 때문에 함수에서 값이 바뀌면 실제 값도 변경된다
- 파이썬은 기본적으로 참조에 의한 전달 BUT 변수의 자료형에 따라 다르게 작동한다
- 불변형: 정수, 부동소수점 숫자, 문자열, 튜플
- 가변형: 리스트, 사전(dict), 집합(set)

**변수의 유효범위**

- 4가지 종류가 있지만 지역변수와 전역변수가 일반적으로 사용된다
- | 범위                         | 설명                                                                |
  | ---------------------------- | ------------------------------------------------------------------- |
  | **지역(Local) 변수**         | 함수 내에서 정의된 변수로, 해당 함수 내에서만 접근 가능             |
  | **인클로징(Enclosing) 변수** | 중첩된 함수에서 바깥쪽(상위) 함수에 정의된 변수                     |
  | **전역(Global) 변수**        | 함수 외부에서 정의된 변수로, 코드 전체에서 접근 가능                |
  | **내장(Built-in) 변수**      | 파이썬이 기본적으로 제공하는 내장 함수 및 변수 (예: `print`, `len`) |
- 지역변수를 함수 외부에서 사용하려고 시도하면 오류가 발생한다
- 전역변수를 함수 내부에서 변경하려고 할 경우 오류가 발생한다(읽기만 가능)
- 함수 내에서 전역변수와 같은 이름의 변수를 사용하려고 시도할 경우 별도의 지역변수로 인식된다
- 전역변수를 함수 내에서 사용(변경)하기 위해서는 `global 전역변수`를 지정하여 변경할 수 있다

**클래스**

- 객체 지향 언어: 데이터와 작업을 한 곳에 모아서 수정의 영향을 최소화, 캡슐화를 통해 불필요한 접근을 제어
- 클래스: 객체의 설계도
- 인스턴스: 클래스를 통해 만들어낸 실제 객체
- `class 클래스명(괄호는 올수도있고 없을 수도 있음):` 형태로 생성
- `__init__`: 생성자, 클래스 당 필수로 존재한다, 데이터를 초기화하는데 사용한다, 객체를 생성할 때 사용한다
- `__del__`: 소멸자, 사용되는 상황은 별로 없다
- 메서드: 함수와 같은 형태로(def) 작성한다, 인수에 self를 반드시 작성해야한다
- 상속
  - 여러클래스가 공통되는 부분을 가지는 경우 해당 부분을 구현하는 기저클래스를 만들어 상속해서 사용한다
  - 클래스 생성 시 `클래스명(부모 클래스)`를 적고, 생성자 내부에 부모 클래스의 생성자를 정의한다
- 접근 속성: public, private 등의 지정은 없지만 변수나 메서드 앞에 \_ , \_\_를 붙이는 방식을 사용한다
- \_\_변수명을 외부에서 참조하려고 할 경우 오류가 발생한다
- 모듈: 함수나 클래스가 적힌 단일 파일, 패키지: 모듈을 모은 것
- 모듈과 패키지는 import 문을 통해 가져와서 사용할 수 있다

**[실습파일](point8_ex.py)**
