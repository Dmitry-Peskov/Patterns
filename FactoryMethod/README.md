![FactoryMethodPattern.png](https://github.com/Dmitry-Peskov/Patterns/blob/main/img/FactoryMethodPattern.png)

**Фабричный метод** (англ. Factory Method), или **виртуальный конструктор** (англ. Virtual Constructor) — 
порождающий шаблон проектирования, предоставляющий подклассам (дочерним классам, субклассам) интерфейс 
для создания экземпляров некоторого класса. В момент создания наследники могут определить, какой класс 
создавать. Иными словами, данный шаблон делегирует создание объектов наследникам родительского класса. 
Это позволяет использовать в коде программы не конкретные классы, а манипулировать абстрактными объектами 
на более высоком уровне.  

### Цель
Определяет интерфейс для создания объекта, но оставляет подклассам решение о том, на основании какого класса создавать объект. Фабричный метод позволяет классу делегировать создание подклассов. Используется, когда:

 - классу заранее неизвестно, объекты каких подклассов ему нужно создавать.
 - класс спроектирован так, чтобы объекты, которые он создаёт, специфицировались подклассами.
 - класс делегирует свои обязанности одному из нескольких вспомогательных подклассов, и планируется локализовать знание о том, какой класс принимает эти обязанности на себя.

### Достоинства
 - позволяет сделать код создания объектов более универсальным, не привязываясь к конкретным классам (ConcreteProduct), а оперируя лишь общим интерфейсом (Product);
 - позволяет установить связь между параллельными иерархиями классов.

### Недостатки
 - необходимость создавать наследника Creator для каждого нового типа продукта (ConcreteProduct).

