# DataScientist_WS

# Сессия 1

1.1 Предобработка данных и выделение значимых атрибутов.
Задача автоматической сортировки корреспонденции заключается в определении адресата для входящих документов. Исходя из этого, необходимо определить, какие атрибуты имеют наибольшее влияние на классификацию входящих документов и оставить только их для последующего обучения. Также необходимо обосновать выбор атрибутов.

Используемые библиотека - pandas, re, matplotlib, pymorphy2, nltk, collections, wordcloud

Анализ данных — это процесс сбора, преобразования, очистки и моделирования данных с целью обнаружения необходимой информации. Полученные результаты сообщаются, предлагая выводы и поддерживая принятие решений. Визуализация данных иногда используется для изображения данных для облегчения обнаружения полезных шаблонов в данных. Термины «Моделирование данных» и «Анализ данных» означают одно и то же.

1.2 Разбиение сложных атрибутов.
В исходных данных есть поля, представляющие собой конкатенацию нескольких, иногда разнотипных, значений. Необходимо выделить и разбить такие поля на несколько других

Удаляем пропущенные значеия, не трогая колонку примечания.

1.3 Дополнение недостающими данными.
Согласно алгоритму направления входящей документации, письма от конкретных лиц и организаций направляются разным сотрудникам Союза. Так, например, от первых лиц министерств – непосредственно Генеральному директору, независимо от указанного адресата. Однако в исходных данных отсутствует информация о том, кем является отправитель. Такая же ситуация с адресатом, система, определяющая направление документа по фамилии будет являться частным случаем решения, и в случае кадровых перестановок не сможет функционировать. В связи с этим, необходимо проанализировать исходный набор данных и дополнить его.

Создаём доп. признаки на основе краткого содержания и даты регистрации, из которой мы можем взять месяц отправки. Переводим дату в datetime. Анализируем дату регистрации.

1.4 Формирование словарей данных.
Сформируйте отдельный атрибут или атрибуты, где будет содержаться анализ краткого содержания документов по количеству вхождений ключевых слов. Проанализируйте возможность определения адресата, используя полученные словари и Перечень вопросов и список руководителей, кому делегировано рассмотрение и подписание ответов.

![image](https://user-images.githubusercontent.com/94251604/155878975-59d42840-5ed8-4b7e-94e1-f84a96e5feca.png)

График

![image](https://user-images.githubusercontent.com/94251604/155878986-1f9255f2-0894-443e-bbb1-c74bd6813bad.png)

Облако слов

1.5 Преобразование списков переадресаций
В исходных данных некоторые письма переадресуются другим сотрудникам. Необходимо выявить такие строки и изменить начального адресата на того, кому в итоге был направлен документ

Вытаскиваем Авторов (от которых исходит письмо). Переписать список откуда и куда, сравнить строки. Анализируем форму составления кратного сожержания

# Сессия 2

2.1 Классификация документов
Выберите модель классификации входящих документов по адресату, приведите обоснование выбора модели. Разделите исходный набор данных на обучающую и тестирующую выборки оптимальным образом.

Выбрал модель Викторизация :D

![image](https://user-images.githubusercontent.com/94251604/155879228-98585ed6-3c43-412b-9d9d-3b48233fb4bf.png)

2.2 Визуализация зависимостей данных
Используя программные средства, визуализируйте зависимости атрибутов в наборе данных.  Визуализация должна отражать влияние атрибутов на определение класса (адресата). Произведите расчеты зависимостей по выбранным алгоритмам. Приведите интерпретацию полученным результатам


![image](https://user-images.githubusercontent.com/94251604/155879267-89429921-6c2b-43b9-8cba-b49e0da2e911.png)


![image](https://user-images.githubusercontent.com/94251604/155879283-ebea93ee-735f-48f9-8f96-5f7ddc93641d.png)


![image](https://user-images.githubusercontent.com/94251604/155879297-88502177-3482-4599-a21d-044142f08568.png)

# Сессия 3

3.1 Обучение
Проведите обучение выбранной модели на обучающей выборке, сформированной в предыдущей сессии. Протестируйте работу обученной модели на тестовой выборке.Определите показатели точности работы выбранной модели, сравните с остальными рассматриваемыми моделями.

![image](https://user-images.githubusercontent.com/94251604/155879381-a3792bdb-5c7f-4e2e-939b-b254fb8353da.png)

Векторизация

![image](https://user-images.githubusercontent.com/94251604/155879477-5fa63134-80d4-4e01-b631-88d0d5651e61.png)

Catboost - Кроссвалидация

<svg width="3426pt" height="479pt" viewBox="0.00 0.00 3425.84 479.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 475)">
<title>%3</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-475 3421.8414,-475 3421.8414,4 -4,4"></polygon>
<!-- 0 -->
<g id="node1" class="node">
<title>0</title>
<ellipse fill="none" stroke="#000000" cx="1678" cy="-453" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="1678" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">219, value&gt;0.0547479</text>
</g>
<!-- 1 -->
<g id="node2" class="node">
<title>1</title>
<ellipse fill="none" stroke="#000000" cx="1254" cy="-366" rx="91.784" ry="18"></ellipse>
<text text-anchor="middle" x="1254" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">69, value&gt;0.0874311</text>
</g>
<!-- 0&#45;&gt;1 -->
<g id="edge1" class="edge">
<title>0-&gt;1</title>
<path fill="none" stroke="#000000" d="M1612.6792,-439.5969C1535.7129,-423.8043 1408.1552,-397.6309 1327.7157,-381.1256"></path>
<polygon fill="#000000" stroke="#000000" points="1328.1602,-377.644 1317.6607,-379.0625 1326.7531,-384.5011 1328.1602,-377.644"></polygon>
<text text-anchor="middle" x="1501.5" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 2 -->
<g id="node3" class="node">
<title>2</title>
<ellipse fill="none" stroke="#000000" cx="2156" cy="-366" rx="91.784" ry="18"></ellipse>
<text text-anchor="middle" x="2156" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">69, value&gt;0.0874311</text>
</g>
<!-- 0&#45;&gt;2 -->
<g id="edge2" class="edge">
<title>0-&gt;2</title>
<path fill="none" stroke="#000000" d="M1747.2499,-440.3959C1835.2835,-424.3731 1986.8234,-396.7916 2078.5875,-380.0897"></path>
<polygon fill="#000000" stroke="#000000" points="2079.4374,-383.4926 2088.649,-378.2584 2078.1839,-376.6058 2079.4374,-383.4926"></polygon>
<text text-anchor="middle" x="1956.5" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 3 -->
<g id="node4" class="node">
<title>3</title>
<ellipse fill="none" stroke="#000000" cx="671" cy="-279" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="671" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">148, value&gt;0.0514966</text>
</g>
<!-- 1&#45;&gt;3 -->
<g id="edge3" class="edge">
<title>1-&gt;3</title>
<path fill="none" stroke="#000000" d="M1180.753,-355.0695C1072.8429,-338.9663 871.5639,-308.9298 756.8597,-291.8127"></path>
<polygon fill="#000000" stroke="#000000" points="757.1227,-288.3132 746.7156,-290.2989 756.0894,-295.2366 757.1227,-288.3132"></polygon>
<text text-anchor="middle" x="1007.5" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 4 -->
<g id="node5" class="node">
<title>4</title>
<ellipse fill="none" stroke="#000000" cx="1254" cy="-279" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="1254" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">148, value&gt;0.0514966</text>
</g>
<!-- 1&#45;&gt;4 -->
<g id="edge4" class="edge">
<title>1-&gt;4</title>
<path fill="none" stroke="#000000" d="M1254,-347.9735C1254,-336.1918 1254,-320.5607 1254,-307.1581"></path>
<polygon fill="#000000" stroke="#000000" points="1257.5001,-307.0033 1254,-297.0034 1250.5001,-307.0034 1257.5001,-307.0033"></polygon>
<text text-anchor="middle" x="1264.5" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 5 -->
<g id="node6" class="node">
<title>5</title>
<ellipse fill="none" stroke="#000000" cx="2156" cy="-279" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="2156" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">148, value&gt;0.0514966</text>
</g>
<!-- 2&#45;&gt;5 -->
<g id="edge5" class="edge">
<title>2-&gt;5</title>
<path fill="none" stroke="#000000" d="M2156,-347.9735C2156,-336.1918 2156,-320.5607 2156,-307.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2159.5001,-307.0033 2156,-297.0034 2152.5001,-307.0034 2159.5001,-307.0033"></polygon>
<text text-anchor="middle" x="2165.5" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 6 -->
<g id="node7" class="node">
<title>6</title>
<ellipse fill="none" stroke="#000000" cx="2738" cy="-279" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="2738" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">148, value&gt;0.0514966</text>
</g>
<!-- 2&#45;&gt;6 -->
<g id="edge6" class="edge">
<title>2-&gt;6</title>
<path fill="none" stroke="#000000" d="M2229.1214,-355.0695C2336.8464,-338.9663 2537.7801,-308.9298 2652.2875,-291.8127"></path>
<polygon fill="#000000" stroke="#000000" points="2653.0417,-295.2389 2662.4143,-290.2989 2652.0067,-288.3159 2653.0417,-295.2389"></polygon>
<text text-anchor="middle" x="2492.5" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 7 -->
<g id="node8" class="node">
<title>7</title>
<ellipse fill="none" stroke="#000000" cx="353" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="353" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 3&#45;&gt;7 -->
<g id="edge7" class="edge">
<title>3-&gt;7</title>
<path fill="none" stroke="#000000" d="M616.3339,-264.0442C560.5176,-248.7737 473.9892,-225.1008 415.4926,-209.097"></path>
<polygon fill="#000000" stroke="#000000" points="416.2023,-205.6626 405.6331,-206.3996 414.3551,-212.4145 416.2023,-205.6626"></polygon>
<text text-anchor="middle" x="541.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 8 -->
<g id="node9" class="node">
<title>8</title>
<ellipse fill="none" stroke="#000000" cx="671" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="671" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 3&#45;&gt;8 -->
<g id="edge8" class="edge">
<title>3-&gt;8</title>
<path fill="none" stroke="#000000" d="M671,-260.9735C671,-249.1918 671,-233.5607 671,-220.1581"></path>
<polygon fill="#000000" stroke="#000000" points="674.5001,-220.0033 671,-210.0034 667.5001,-220.0034 674.5001,-220.0033"></polygon>
<text text-anchor="middle" x="681.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 9 -->
<g id="node10" class="node">
<title>9</title>
<ellipse fill="none" stroke="#000000" cx="1201" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="1201" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 4&#45;&gt;9 -->
<g id="edge9" class="edge">
<title>4-&gt;9</title>
<path fill="none" stroke="#000000" d="M1243.0184,-260.9735C1235.5567,-248.7252 1225.5606,-232.3165 1217.1903,-218.5766"></path>
<polygon fill="#000000" stroke="#000000" points="1220.1592,-216.7225 1211.9676,-210.0034 1214.1812,-220.3644 1220.1592,-216.7225"></polygon>
<text text-anchor="middle" x="1240.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 10 -->
<g id="node11" class="node">
<title>10</title>
<ellipse fill="none" stroke="#000000" cx="1413" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="1413" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 4&#45;&gt;10 -->
<g id="edge10" class="edge">
<title>4-&gt;10</title>
<path fill="none" stroke="#000000" d="M1285.4133,-261.8116C1310.6197,-248.0194 1346.1569,-228.5745 1373.3267,-213.708"></path>
<polygon fill="#000000" stroke="#000000" points="1375.1004,-216.7272 1382.193,-208.8567 1371.7403,-210.5864 1375.1004,-216.7272"></polygon>
<text text-anchor="middle" x="1354.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 11 -->
<g id="node12" class="node">
<title>11</title>
<ellipse fill="none" stroke="#000000" cx="2049" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="2049" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 5&#45;&gt;11 -->
<g id="edge11" class="edge">
<title>5-&gt;11</title>
<path fill="none" stroke="#000000" d="M2134.347,-261.3943C2118.2485,-248.3048 2096.1013,-230.2973 2078.4022,-215.9064"></path>
<polygon fill="#000000" stroke="#000000" points="2080.5878,-213.1726 2070.6208,-209.5796 2076.1717,-218.6039 2080.5878,-213.1726"></polygon>
<text text-anchor="middle" x="2118.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 12 -->
<g id="node13" class="node">
<title>12</title>
<ellipse fill="none" stroke="#000000" cx="2261" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="2261" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 5&#45;&gt;12 -->
<g id="edge12" class="edge">
<title>5-&gt;12</title>
<path fill="none" stroke="#000000" d="M2177.2483,-261.3943C2192.9036,-248.4228 2214.388,-230.6213 2231.6769,-216.2962"></path>
<polygon fill="#000000" stroke="#000000" points="2234.3161,-218.6549 2239.7833,-209.5796 2229.85,-213.2647 2234.3161,-218.6549"></polygon>
<text text-anchor="middle" x="2225.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 13 -->
<g id="node14" class="node">
<title>13</title>
<ellipse fill="none" stroke="#000000" cx="2738" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="2738" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 6&#45;&gt;13 -->
<g id="edge13" class="edge">
<title>6-&gt;13</title>
<path fill="none" stroke="#000000" d="M2738,-260.9735C2738,-249.1918 2738,-233.5607 2738,-220.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2741.5001,-220.0033 2738,-210.0034 2734.5001,-220.0034 2741.5001,-220.0033"></polygon>
<text text-anchor="middle" x="2747.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 14 -->
<g id="node15" class="node">
<title>14</title>
<ellipse fill="none" stroke="#000000" cx="3109" cy="-192" rx="87.1846" ry="18"></ellipse>
<text text-anchor="middle" x="3109" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">54, value&gt;0.590764</text>
</g>
<!-- 6&#45;&gt;14 -->
<g id="edge14" class="edge">
<title>6-&gt;14</title>
<path fill="none" stroke="#000000" d="M2798.4333,-264.8283C2865.0698,-249.202 2972.0103,-224.1243 3041.3866,-207.8554"></path>
<polygon fill="#000000" stroke="#000000" points="3042.4038,-211.2119 3051.3406,-205.5212 3040.8056,-204.3968 3042.4038,-211.2119"></polygon>
<text text-anchor="middle" x="2956.5" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 15 -->
<g id="node16" class="node">
<title>15</title>
<ellipse fill="none" stroke="#000000" cx="141" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="141" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 7&#45;&gt;15 -->
<g id="edge15" class="edge">
<title>7-&gt;15</title>
<path fill="none" stroke="#000000" d="M313.6213,-175.8399C278.9961,-161.6305 228.4218,-140.8759 190.9575,-125.5014"></path>
<polygon fill="#000000" stroke="#000000" points="191.8288,-122.0758 181.2487,-121.5171 189.1712,-128.5517 191.8288,-122.0758"></polygon>
<text text-anchor="middle" x="269.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 16 -->
<g id="node17" class="node">
<title>16</title>
<ellipse fill="none" stroke="#000000" cx="353" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="353" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 7&#45;&gt;16 -->
<g id="edge16" class="edge">
<title>7-&gt;16</title>
<path fill="none" stroke="#000000" d="M353,-173.9735C353,-162.1918 353,-146.5607 353,-133.1581"></path>
<polygon fill="#000000" stroke="#000000" points="356.5001,-133.0033 353,-123.0034 349.5001,-133.0034 356.5001,-133.0033"></polygon>
<text text-anchor="middle" x="363.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 17 -->
<g id="node18" class="node">
<title>17</title>
<ellipse fill="none" stroke="#000000" cx="565" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="565" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 8&#45;&gt;17 -->
<g id="edge17" class="edge">
<title>8-&gt;17</title>
<path fill="none" stroke="#000000" d="M649.5493,-174.3943C633.745,-161.4228 612.0559,-143.6213 594.6023,-129.2962"></path>
<polygon fill="#000000" stroke="#000000" points="596.3691,-126.2184 586.4188,-122.5796 591.9281,-131.6293 596.3691,-126.2184"></polygon>
<text text-anchor="middle" x="634.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 18 -->
<g id="node19" class="node">
<title>18</title>
<ellipse fill="none" stroke="#000000" cx="777" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="777" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 8&#45;&gt;18 -->
<g id="edge18" class="edge">
<title>8-&gt;18</title>
<path fill="none" stroke="#000000" d="M692.4507,-174.3943C708.255,-161.4228 729.9441,-143.6213 747.3977,-129.2962"></path>
<polygon fill="#000000" stroke="#000000" points="750.0719,-131.6293 755.5812,-122.5796 745.6309,-126.2184 750.0719,-131.6293"></polygon>
<text text-anchor="middle" x="741.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 19 -->
<g id="node20" class="node">
<title>19</title>
<ellipse fill="none" stroke="#000000" cx="989" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="989" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 9&#45;&gt;19 -->
<g id="edge19" class="edge">
<title>9-&gt;19</title>
<path fill="none" stroke="#000000" d="M1161.6213,-175.8399C1126.9961,-161.6305 1076.4218,-140.8759 1038.9575,-125.5014"></path>
<polygon fill="#000000" stroke="#000000" points="1039.8288,-122.0758 1029.2487,-121.5171 1037.1712,-128.5517 1039.8288,-122.0758"></polygon>
<text text-anchor="middle" x="1117.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 20 -->
<g id="node21" class="node">
<title>20</title>
<ellipse fill="none" stroke="#000000" cx="1201" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="1201" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 9&#45;&gt;20 -->
<g id="edge20" class="edge">
<title>9-&gt;20</title>
<path fill="none" stroke="#000000" d="M1201,-173.9735C1201,-162.1918 1201,-146.5607 1201,-133.1581"></path>
<polygon fill="#000000" stroke="#000000" points="1204.5001,-133.0033 1201,-123.0034 1197.5001,-133.0034 1204.5001,-133.0033"></polygon>
<text text-anchor="middle" x="1211.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 21 -->
<g id="node22" class="node">
<title>21</title>
<ellipse fill="none" stroke="#000000" cx="1413" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="1413" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 10&#45;&gt;21 -->
<g id="edge21" class="edge">
<title>10-&gt;21</title>
<path fill="none" stroke="#000000" d="M1413,-173.9735C1413,-162.1918 1413,-146.5607 1413,-133.1581"></path>
<polygon fill="#000000" stroke="#000000" points="1416.5001,-133.0033 1413,-123.0034 1409.5001,-133.0034 1416.5001,-133.0033"></polygon>
<text text-anchor="middle" x="1422.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 22 -->
<g id="node23" class="node">
<title>22</title>
<ellipse fill="none" stroke="#000000" cx="1625" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="1625" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 10&#45;&gt;22 -->
<g id="edge22" class="edge">
<title>10-&gt;22</title>
<path fill="none" stroke="#000000" d="M1452.3787,-175.8399C1487.0039,-161.6305 1537.5782,-140.8759 1575.0425,-125.5014"></path>
<polygon fill="#000000" stroke="#000000" points="1576.8288,-128.5517 1584.7513,-121.5171 1574.1712,-122.0758 1576.8288,-128.5517"></polygon>
<text text-anchor="middle" x="1542.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 23 -->
<g id="node24" class="node">
<title>23</title>
<ellipse fill="none" stroke="#000000" cx="1837" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="1837" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 11&#45;&gt;23 -->
<g id="edge23" class="edge">
<title>11-&gt;23</title>
<path fill="none" stroke="#000000" d="M2009.6213,-175.8399C1974.9961,-161.6305 1924.4218,-140.8759 1886.9575,-125.5014"></path>
<polygon fill="#000000" stroke="#000000" points="1887.8288,-122.0758 1877.2487,-121.5171 1885.1712,-128.5517 1887.8288,-122.0758"></polygon>
<text text-anchor="middle" x="1965.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 24 -->
<g id="node25" class="node">
<title>24</title>
<ellipse fill="none" stroke="#000000" cx="2049" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="2049" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 11&#45;&gt;24 -->
<g id="edge24" class="edge">
<title>11-&gt;24</title>
<path fill="none" stroke="#000000" d="M2049,-173.9735C2049,-162.1918 2049,-146.5607 2049,-133.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2052.5001,-133.0033 2049,-123.0034 2045.5001,-133.0034 2052.5001,-133.0033"></polygon>
<text text-anchor="middle" x="2059.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 25 -->
<g id="node26" class="node">
<title>25</title>
<ellipse fill="none" stroke="#000000" cx="2261" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="2261" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 12&#45;&gt;25 -->
<g id="edge25" class="edge">
<title>12-&gt;25</title>
<path fill="none" stroke="#000000" d="M2261,-173.9735C2261,-162.1918 2261,-146.5607 2261,-133.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2264.5001,-133.0033 2261,-123.0034 2257.5001,-133.0034 2264.5001,-133.0033"></polygon>
<text text-anchor="middle" x="2270.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 26 -->
<g id="node27" class="node">
<title>26</title>
<ellipse fill="none" stroke="#000000" cx="2473" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="2473" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 12&#45;&gt;26 -->
<g id="edge26" class="edge">
<title>12-&gt;26</title>
<path fill="none" stroke="#000000" d="M2300.3787,-175.8399C2335.0039,-161.6305 2385.5782,-140.8759 2423.0425,-125.5014"></path>
<polygon fill="#000000" stroke="#000000" points="2424.8288,-128.5517 2432.7513,-121.5171 2422.1712,-122.0758 2424.8288,-128.5517"></polygon>
<text text-anchor="middle" x="2390.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 27 -->
<g id="node28" class="node">
<title>27</title>
<ellipse fill="none" stroke="#000000" cx="2685" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="2685" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 13&#45;&gt;27 -->
<g id="edge27" class="edge">
<title>13-&gt;27</title>
<path fill="none" stroke="#000000" d="M2727.0184,-173.9735C2719.5567,-161.7252 2709.5606,-145.3165 2701.1903,-131.5766"></path>
<polygon fill="#000000" stroke="#000000" points="2704.1592,-129.7225 2695.9676,-123.0034 2698.1812,-133.3644 2704.1592,-129.7225"></polygon>
<text text-anchor="middle" x="2724.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 28 -->
<g id="node29" class="node">
<title>28</title>
<ellipse fill="none" stroke="#000000" cx="2897" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="2897" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 13&#45;&gt;28 -->
<g id="edge28" class="edge">
<title>13-&gt;28</title>
<path fill="none" stroke="#000000" d="M2769.0343,-175.019C2794.1239,-161.2907 2829.6276,-141.8641 2856.8756,-126.9549"></path>
<polygon fill="#000000" stroke="#000000" points="2858.6802,-129.9572 2865.7727,-122.0866 2855.32,-123.8164 2858.6802,-129.9572"></polygon>
<text text-anchor="middle" x="2838.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 29 -->
<g id="node30" class="node">
<title>29</title>
<ellipse fill="none" stroke="#000000" cx="3109" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="3109" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 14&#45;&gt;29 -->
<g id="edge29" class="edge">
<title>14-&gt;29</title>
<path fill="none" stroke="#000000" d="M3109,-173.9735C3109,-162.1918 3109,-146.5607 3109,-133.1581"></path>
<polygon fill="#000000" stroke="#000000" points="3112.5001,-133.0033 3109,-123.0034 3105.5001,-133.0034 3112.5001,-133.0033"></polygon>
<text text-anchor="middle" x="3118.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 30 -->
<g id="node31" class="node">
<title>30</title>
<ellipse fill="none" stroke="#000000" cx="3321" cy="-105" rx="96.6831" ry="18"></ellipse>
<text text-anchor="middle" x="3321" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">190, value&gt;0.0358345</text>
</g>
<!-- 14&#45;&gt;30 -->
<g id="edge30" class="edge">
<title>14-&gt;30</title>
<path fill="none" stroke="#000000" d="M3148.3787,-175.8399C3183.0039,-161.6305 3233.5782,-140.8759 3271.0425,-125.5014"></path>
<polygon fill="#000000" stroke="#000000" points="3272.8288,-128.5517 3280.7513,-121.5171 3270.1712,-122.0758 3272.8288,-128.5517"></polygon>
<text text-anchor="middle" x="3238.5" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 31 -->
<g id="node32" class="node">
<title>31</title>
<polygon fill="none" stroke="#ff0000" points="88,-36 0,-36 0,0 88,0 88,-36"></polygon>
<text text-anchor="middle" x="44" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = -0.008</text>
</g>
<!-- 15&#45;&gt;31 -->
<g id="edge31" class="edge">
<title>15-&gt;31</title>
<path fill="none" stroke="#000000" d="M120.9015,-86.9735C106.7251,-74.2586 87.55,-57.0603 71.8939,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="73.8541,-40.0748 64.0727,-36.0034 69.1802,-45.2859 73.8541,-40.0748"></polygon>
<text text-anchor="middle" x="108.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 32 -->
<g id="node33" class="node">
<title>32</title>
<polygon fill="none" stroke="#ff0000" points="189.5,-36 106.5,-36 106.5,0 189.5,0 189.5,-36"></polygon>
<text text-anchor="middle" x="148" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.006</text>
</g>
<!-- 15&#45;&gt;32 -->
<g id="edge32" class="edge">
<title>15-&gt;32</title>
<path fill="none" stroke="#000000" d="M142.4504,-86.9735C143.3984,-75.1918 144.656,-59.5607 145.7344,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="149.2381,-46.2519 146.5515,-36.0034 142.2606,-45.6904 149.2381,-46.2519"></polygon>
<text text-anchor="middle" x="155.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 33 -->
<g id="node34" class="node">
<title>33</title>
<polygon fill="none" stroke="#ff0000" points="295.5,-36 212.5,-36 212.5,0 295.5,0 295.5,-36"></polygon>
<text text-anchor="middle" x="254" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.005</text>
</g>
<!-- 16&#45;&gt;33 -->
<g id="edge33" class="edge">
<title>16-&gt;33</title>
<path fill="none" stroke="#000000" d="M332.4871,-86.9735C317.8856,-74.1419 298.0884,-56.7443 282.0302,-42.6326"></path>
<polygon fill="#000000" stroke="#000000" points="284.3087,-39.9755 274.4866,-36.0034 279.6878,-45.2336 284.3087,-39.9755"></polygon>
<text text-anchor="middle" x="319.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 34 -->
<g id="node35" class="node">
<title>34</title>
<polygon fill="none" stroke="#ff0000" points="396.5,-36 313.5,-36 313.5,0 396.5,0 396.5,-36"></polygon>
<text text-anchor="middle" x="355" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.002</text>
</g>
<!-- 16&#45;&gt;34 -->
<g id="edge34" class="edge">
<title>16-&gt;34</title>
<path fill="none" stroke="#000000" d="M353.4144,-86.9735C353.6852,-75.1918 354.0446,-59.5607 354.3527,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="357.8553,-46.0812 354.5861,-36.0034 350.8571,-45.9202 357.8553,-46.0812"></polygon>
<text text-anchor="middle" x="365.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 35 -->
<g id="node36" class="node">
<title>35</title>
<polygon fill="none" stroke="#ff0000" points="511,-36 423,-36 423,0 511,0 511,-36"></polygon>
<text text-anchor="middle" x="467" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = -0.005</text>
</g>
<!-- 17&#45;&gt;35 -->
<g id="edge35" class="edge">
<title>17-&gt;35</title>
<path fill="none" stroke="#000000" d="M544.6943,-86.9735C530.3717,-74.2586 510.9989,-57.0603 495.1815,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="497.0816,-40.0249 487.2797,-36.0034 492.4343,-45.2597 497.0816,-40.0249"></polygon>
<text text-anchor="middle" x="531.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 36 -->
<g id="node37" class="node">
<title>36</title>
<polygon fill="none" stroke="#ff0000" points="612.5,-36 529.5,-36 529.5,0 612.5,0 612.5,-36"></polygon>
<text text-anchor="middle" x="571" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 17&#45;&gt;36 -->
<g id="edge36" class="edge">
<title>17-&gt;36</title>
<path fill="none" stroke="#000000" d="M566.2432,-86.9735C567.0557,-75.1918 568.1337,-59.5607 569.0581,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="572.562,-46.2205 569.7584,-36.0034 565.5786,-45.7388 572.562,-46.2205"></polygon>
<text text-anchor="middle" x="579.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 37 -->
<g id="node38" class="node">
<title>37</title>
<polygon fill="none" stroke="#ff0000" points="742.5,-36 659.5,-36 659.5,0 742.5,0 742.5,-36"></polygon>
<text text-anchor="middle" x="701" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 18&#45;&gt;37 -->
<g id="edge37" class="edge">
<title>18-&gt;37</title>
<path fill="none" stroke="#000000" d="M761.2528,-86.9735C750.3492,-74.4919 735.6716,-57.6899 723.533,-43.7944"></path>
<polygon fill="#000000" stroke="#000000" points="725.9419,-41.2319 716.7271,-36.0034 720.6701,-45.8371 725.9419,-41.2319"></polygon>
<text text-anchor="middle" x="753.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 38 -->
<g id="node39" class="node">
<title>38</title>
<polygon fill="none" stroke="#ff0000" points="843.5,-36 760.5,-36 760.5,0 843.5,0 843.5,-36"></polygon>
<text text-anchor="middle" x="802" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 18&#45;&gt;38 -->
<g id="edge38" class="edge">
<title>18-&gt;38</title>
<path fill="none" stroke="#000000" d="M782.18,-86.9735C785.5991,-75.0751 790.1463,-59.2508 794.0228,-45.7606"></path>
<polygon fill="#000000" stroke="#000000" points="797.4286,-46.5811 796.8266,-36.0034 790.7009,-44.6478 797.4286,-46.5811"></polygon>
<text text-anchor="middle" x="801.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 39 -->
<g id="node40" class="node">
<title>39</title>
<polygon fill="none" stroke="#ff0000" points="958.5,-36 875.5,-36 875.5,0 958.5,0 958.5,-36"></polygon>
<text text-anchor="middle" x="917" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 19&#45;&gt;39 -->
<g id="edge39" class="edge">
<title>19-&gt;39</title>
<path fill="none" stroke="#000000" d="M974.0816,-86.9735C963.7519,-74.4919 949.8468,-57.6899 938.3471,-43.7944"></path>
<polygon fill="#000000" stroke="#000000" points="940.9714,-41.4758 931.8993,-36.0034 935.5787,-45.9388 940.9714,-41.4758"></polygon>
<text text-anchor="middle" x="967.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 40 -->
<g id="node41" class="node">
<title>40</title>
<polygon fill="none" stroke="#ff0000" points="1065,-36 977,-36 977,0 1065,0 1065,-36"></polygon>
<text text-anchor="middle" x="1021" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = -0.005</text>
</g>
<!-- 19&#45;&gt;40 -->
<g id="edge40" class="edge">
<title>19-&gt;40</title>
<path fill="none" stroke="#000000" d="M995.6304,-86.9735C1000.0069,-75.0751 1005.8273,-59.2508 1010.7892,-45.7606"></path>
<polygon fill="#000000" stroke="#000000" points="1014.2108,-46.5969 1014.3781,-36.0034 1007.6411,-44.1804 1014.2108,-46.5969"></polygon>
<text text-anchor="middle" x="1017.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 41 -->
<g id="node42" class="node">
<title>41</title>
<polygon fill="none" stroke="#ff0000" points="1173.5,-36 1090.5,-36 1090.5,0 1173.5,0 1173.5,-36"></polygon>
<text text-anchor="middle" x="1132" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 20&#45;&gt;41 -->
<g id="edge41" class="edge">
<title>20-&gt;41</title>
<path fill="none" stroke="#000000" d="M1186.7032,-86.9735C1176.8964,-74.6085 1163.727,-58.0036 1152.7672,-44.1847"></path>
<polygon fill="#000000" stroke="#000000" points="1155.2348,-41.6635 1146.2785,-36.0034 1149.7503,-46.0133 1155.2348,-41.6635"></polygon>
<text text-anchor="middle" x="1180.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 42 -->
<g id="node43" class="node">
<title>42</title>
<polygon fill="none" stroke="#ff0000" points="1274.5,-36 1191.5,-36 1191.5,0 1274.5,0 1274.5,-36"></polygon>
<text text-anchor="middle" x="1233" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 20&#45;&gt;42 -->
<g id="edge42" class="edge">
<title>20-&gt;42</title>
<path fill="none" stroke="#000000" d="M1207.6304,-86.9735C1212.0069,-75.0751 1217.8273,-59.2508 1222.7892,-45.7606"></path>
<polygon fill="#000000" stroke="#000000" points="1226.2108,-46.5969 1226.3781,-36.0034 1219.6411,-44.1804 1226.2108,-46.5969"></polygon>
<text text-anchor="middle" x="1229.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 43 -->
<g id="node44" class="node">
<title>43</title>
<polygon fill="none" stroke="#ff0000" points="1379.5,-36 1296.5,-36 1296.5,0 1379.5,0 1379.5,-36"></polygon>
<text text-anchor="middle" x="1338" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 21&#45;&gt;43 -->
<g id="edge43" class="edge">
<title>21-&gt;43</title>
<path fill="none" stroke="#000000" d="M1397.46,-86.9735C1386.6999,-74.4919 1372.2154,-57.6899 1360.2365,-43.7944"></path>
<polygon fill="#000000" stroke="#000000" points="1362.7005,-41.2922 1353.5201,-36.0034 1357.3986,-45.8628 1362.7005,-41.2922"></polygon>
<text text-anchor="middle" x="1389.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 44 -->
<g id="node45" class="node">
<title>44</title>
<polygon fill="none" stroke="#ff0000" points="1480.5,-36 1397.5,-36 1397.5,0 1480.5,0 1480.5,-36"></polygon>
<text text-anchor="middle" x="1439" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 21&#45;&gt;44 -->
<g id="edge44" class="edge">
<title>21-&gt;44</title>
<path fill="none" stroke="#000000" d="M1418.3872,-86.9735C1421.9431,-75.0751 1426.6722,-59.2508 1430.7037,-45.7606"></path>
<polygon fill="#000000" stroke="#000000" points="1434.1097,-46.5869 1433.6197,-36.0034 1427.4028,-44.5825 1434.1097,-46.5869"></polygon>
<text text-anchor="middle" x="1438.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 45 -->
<g id="node46" class="node">
<title>45</title>
<polygon fill="none" stroke="#ff0000" points="1583.5,-36 1500.5,-36 1500.5,0 1583.5,0 1583.5,-36"></polygon>
<text text-anchor="middle" x="1542" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 22&#45;&gt;45 -->
<g id="edge45" class="edge">
<title>22-&gt;45</title>
<path fill="none" stroke="#000000" d="M1607.8023,-86.9735C1595.7833,-74.3752 1579.5651,-57.3755 1566.2375,-43.4055"></path>
<polygon fill="#000000" stroke="#000000" points="1568.6108,-40.8228 1559.1756,-36.0034 1563.546,-45.6548 1568.6108,-40.8228"></polygon>
<text text-anchor="middle" x="1598.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 46 -->
<g id="node47" class="node">
<title>46</title>
<polygon fill="none" stroke="#ff0000" points="1684.5,-36 1601.5,-36 1601.5,0 1684.5,0 1684.5,-36"></polygon>
<text text-anchor="middle" x="1643" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 22&#45;&gt;46 -->
<g id="edge46" class="edge">
<title>22-&gt;46</title>
<path fill="none" stroke="#000000" d="M1628.7296,-86.9735C1631.1672,-75.1918 1634.4012,-59.5607 1637.1742,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="1640.6764,-46.5051 1639.2752,-36.0034 1633.8216,-45.0868 1640.6764,-46.5051"></polygon>
<text text-anchor="middle" x="1646.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 47 -->
<g id="node48" class="node">
<title>47</title>
<polygon fill="none" stroke="#ff0000" points="1792,-36 1704,-36 1704,0 1792,0 1792,-36"></polygon>
<text text-anchor="middle" x="1748" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = -0.005</text>
</g>
<!-- 23&#45;&gt;47 -->
<g id="edge47" class="edge">
<title>23-&gt;47</title>
<path fill="none" stroke="#000000" d="M1818.5591,-86.9735C1805.5519,-74.2586 1787.9582,-57.0603 1773.5934,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="1776.0148,-40.4908 1766.4172,-36.0034 1771.1216,-45.4965 1776.0148,-40.4908"></polygon>
<text text-anchor="middle" x="1807.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 48 -->
<g id="node49" class="node">
<title>48</title>
<polygon fill="none" stroke="#ff0000" points="1893.5,-36 1810.5,-36 1810.5,0 1893.5,0 1893.5,-36"></polygon>
<text text-anchor="middle" x="1852" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 23&#45;&gt;48 -->
<g id="edge48" class="edge">
<title>23-&gt;48</title>
<path fill="none" stroke="#000000" d="M1840.108,-86.9735C1842.1393,-75.1918 1844.8344,-59.5607 1847.1452,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="1850.6459,-46.4527 1848.896,-36.0034 1843.7477,-45.2633 1850.6459,-46.4527"></polygon>
<text text-anchor="middle" x="1856.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 49 -->
<g id="node50" class="node">
<title>49</title>
<polygon fill="none" stroke="#ff0000" points="1994.5,-36 1911.5,-36 1911.5,0 1994.5,0 1994.5,-36"></polygon>
<text text-anchor="middle" x="1953" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 24&#45;&gt;49 -->
<g id="edge49" class="edge">
<title>24-&gt;49</title>
<path fill="none" stroke="#000000" d="M2029.1087,-86.9735C2015.0784,-74.2586 1996.101,-57.0603 1980.6064,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="1982.626,-40.1251 1972.8658,-36.0034 1977.9253,-45.3121 1982.626,-40.1251"></polygon>
<text text-anchor="middle" x="2016.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 50 -->
<g id="node51" class="node">
<title>50</title>
<polygon fill="none" stroke="#ff0000" points="2095.5,-36 2012.5,-36 2012.5,0 2095.5,0 2095.5,-36"></polygon>
<text text-anchor="middle" x="2054" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 24&#45;&gt;50 -->
<g id="edge50" class="edge">
<title>24-&gt;50</title>
<path fill="none" stroke="#000000" d="M2050.036,-86.9735C2050.7131,-75.1918 2051.6115,-59.5607 2052.3817,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2055.8857,-46.1877 2052.9653,-36.0034 2048.8972,-45.786 2055.8857,-46.1877"></polygon>
<text text-anchor="middle" x="2062.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 51 -->
<g id="node52" class="node">
<title>51</title>
<polygon fill="none" stroke="#ff0000" points="2206.5,-36 2123.5,-36 2123.5,0 2206.5,0 2206.5,-36"></polygon>
<text text-anchor="middle" x="2165" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 25&#45;&gt;51 -->
<g id="edge51" class="edge">
<title>25-&gt;51</title>
<path fill="none" stroke="#000000" d="M2241.1087,-86.9735C2227.0784,-74.2586 2208.101,-57.0603 2192.6064,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="2194.626,-40.1251 2184.8658,-36.0034 2189.9253,-45.3121 2194.626,-40.1251"></polygon>
<text text-anchor="middle" x="2228.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 52 -->
<g id="node53" class="node">
<title>52</title>
<polygon fill="none" stroke="#ff0000" points="2307.5,-36 2224.5,-36 2224.5,0 2307.5,0 2307.5,-36"></polygon>
<text text-anchor="middle" x="2266" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 25&#45;&gt;52 -->
<g id="edge52" class="edge">
<title>25-&gt;52</title>
<path fill="none" stroke="#000000" d="M2262.036,-86.9735C2262.7131,-75.1918 2263.6115,-59.5607 2264.3817,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2267.8857,-46.1877 2264.9653,-36.0034 2260.8972,-45.786 2267.8857,-46.1877"></polygon>
<text text-anchor="middle" x="2274.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 53 -->
<g id="node54" class="node">
<title>53</title>
<polygon fill="none" stroke="#ff0000" points="2418.5,-36 2335.5,-36 2335.5,0 2418.5,0 2418.5,-36"></polygon>
<text text-anchor="middle" x="2377" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 26&#45;&gt;53 -->
<g id="edge53" class="edge">
<title>26-&gt;53</title>
<path fill="none" stroke="#000000" d="M2453.1087,-86.9735C2439.0784,-74.2586 2420.101,-57.0603 2404.6064,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="2406.626,-40.1251 2396.8658,-36.0034 2401.9253,-45.3121 2406.626,-40.1251"></polygon>
<text text-anchor="middle" x="2440.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 54 -->
<g id="node55" class="node">
<title>54</title>
<polygon fill="none" stroke="#ff0000" points="2519.5,-36 2436.5,-36 2436.5,0 2519.5,0 2519.5,-36"></polygon>
<text text-anchor="middle" x="2478" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 26&#45;&gt;54 -->
<g id="edge54" class="edge">
<title>26-&gt;54</title>
<path fill="none" stroke="#000000" d="M2474.036,-86.9735C2474.7131,-75.1918 2475.6115,-59.5607 2476.3817,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2479.8857,-46.1877 2476.9653,-36.0034 2472.8972,-45.786 2479.8857,-46.1877"></polygon>
<text text-anchor="middle" x="2486.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 55 -->
<g id="node56" class="node">
<title>55</title>
<polygon fill="none" stroke="#ff0000" points="2630.5,-36 2547.5,-36 2547.5,0 2630.5,0 2630.5,-36"></polygon>
<text text-anchor="middle" x="2589" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 27&#45;&gt;55 -->
<g id="edge55" class="edge">
<title>27-&gt;55</title>
<path fill="none" stroke="#000000" d="M2665.1087,-86.9735C2651.0784,-74.2586 2632.101,-57.0603 2616.6064,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="2618.626,-40.1251 2608.8658,-36.0034 2613.9253,-45.3121 2618.626,-40.1251"></polygon>
<text text-anchor="middle" x="2652.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 56 -->
<g id="node57" class="node">
<title>56</title>
<polygon fill="none" stroke="#ff0000" points="2731.5,-36 2648.5,-36 2648.5,0 2731.5,0 2731.5,-36"></polygon>
<text text-anchor="middle" x="2690" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 27&#45;&gt;56 -->
<g id="edge56" class="edge">
<title>27-&gt;56</title>
<path fill="none" stroke="#000000" d="M2686.036,-86.9735C2686.7131,-75.1918 2687.6115,-59.5607 2688.3817,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2691.8857,-46.1877 2688.9653,-36.0034 2684.8972,-45.786 2691.8857,-46.1877"></polygon>
<text text-anchor="middle" x="2698.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 57 -->
<g id="node58" class="node">
<title>57</title>
<polygon fill="none" stroke="#ff0000" points="2844.5,-36 2761.5,-36 2761.5,0 2844.5,0 2844.5,-36"></polygon>
<text text-anchor="middle" x="2803" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 28&#45;&gt;57 -->
<g id="edge57" class="edge">
<title>28-&gt;57</title>
<path fill="none" stroke="#000000" d="M2877.5231,-86.9735C2863.7851,-74.2586 2845.2031,-57.0603 2830.0312,-43.0183"></path>
<polygon fill="#000000" stroke="#000000" points="2832.1684,-40.2272 2822.4519,-36.0034 2827.4136,-45.3646 2832.1684,-40.2272"></polygon>
<text text-anchor="middle" x="2865.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 58 -->
<g id="node59" class="node">
<title>58</title>
<polygon fill="none" stroke="#ff0000" points="2945.5,-36 2862.5,-36 2862.5,0 2945.5,0 2945.5,-36"></polygon>
<text text-anchor="middle" x="2904" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 28&#45;&gt;58 -->
<g id="edge58" class="edge">
<title>28-&gt;58</title>
<path fill="none" stroke="#000000" d="M2898.4504,-86.9735C2899.3984,-75.1918 2900.656,-59.5607 2901.7344,-46.1581"></path>
<polygon fill="#000000" stroke="#000000" points="2905.2381,-46.2519 2902.5515,-36.0034 2898.2606,-45.6904 2905.2381,-46.2519"></polygon>
<text text-anchor="middle" x="2911.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 59 -->
<g id="node60" class="node">
<title>59</title>
<polygon fill="none" stroke="#ff0000" points="3102.5,-36 3019.5,-36 3019.5,0 3102.5,0 3102.5,-36"></polygon>
<text text-anchor="middle" x="3061" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 29&#45;&gt;59 -->
<g id="edge59" class="edge">
<title>29-&gt;59</title>
<path fill="none" stroke="#000000" d="M3099.0544,-86.9735C3092.361,-74.8418 3083.4158,-58.6287 3075.8799,-44.9698"></path>
<polygon fill="#000000" stroke="#000000" points="3078.8282,-43.0684 3070.9329,-36.0034 3072.6992,-46.4499 3078.8282,-43.0684"></polygon>
<text text-anchor="middle" x="3097.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 60 -->
<g id="node61" class="node">
<title>60</title>
<polygon fill="none" stroke="#ff0000" points="3203.5,-36 3120.5,-36 3120.5,0 3203.5,0 3203.5,-36"></polygon>
<text text-anchor="middle" x="3162" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 29&#45;&gt;60 -->
<g id="edge60" class="edge">
<title>29-&gt;60</title>
<path fill="none" stroke="#000000" d="M3119.9816,-86.9735C3127.4433,-74.7252 3137.4394,-58.3165 3145.8097,-44.5766"></path>
<polygon fill="#000000" stroke="#000000" points="3148.8188,-46.3644 3151.0324,-36.0034 3142.8408,-42.7225 3148.8188,-46.3644"></polygon>
<text text-anchor="middle" x="3149.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
<!-- 61 -->
<g id="node62" class="node">
<title>61</title>
<polygon fill="none" stroke="#ff0000" points="3309.5,-36 3226.5,-36 3226.5,0 3309.5,0 3309.5,-36"></polygon>
<text text-anchor="middle" x="3268" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 30&#45;&gt;61 -->
<g id="edge61" class="edge">
<title>30-&gt;61</title>
<path fill="none" stroke="#000000" d="M3310.0184,-86.9735C3302.5567,-74.7252 3292.5606,-58.3165 3284.1903,-44.5766"></path>
<polygon fill="#000000" stroke="#000000" points="3287.1592,-42.7225 3278.9676,-36.0034 3281.1812,-46.3644 3287.1592,-42.7225"></polygon>
<text text-anchor="middle" x="3307.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">No</text>
</g>
<!-- 62 -->
<g id="node63" class="node">
<title>62</title>
<polygon fill="none" stroke="#ff0000" points="3410.5,-36 3327.5,-36 3327.5,0 3410.5,0 3410.5,-36"></polygon>
<text text-anchor="middle" x="3369" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">val = 0.000</text>
</g>
<!-- 30&#45;&gt;62 -->
<g id="edge62" class="edge">
<title>30-&gt;62</title>
<path fill="none" stroke="#000000" d="M3330.9456,-86.9735C3337.639,-74.8418 3346.5842,-58.6287 3354.1201,-44.9698"></path>
<polygon fill="#000000" stroke="#000000" points="3357.3008,-46.4499 3359.0671,-36.0034 3351.1718,-43.0684 3357.3008,-46.4499"></polygon>
<text text-anchor="middle" x="3357.5" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">Yes</text>
</g>
</g>
</svg>

3.2FeatureEngineering
Путём преобразования набора данных, добейтесь более точной работы выбранной модели. Опишите приемы генерации новых данных и результаты, к которым они привели, рассматривая все ранее определенные показатели точности

3.3Подготовка отчета
Подготовьте отчет, содержащий следующие пункты:
	Выбор показателей точности работы модели
	Точность работы выбранной модели в сравнении с другими рассматриваемыми моделями
	Результаты FeatureEngineering

# Сессия 4

4.1 Разработка бота
Вам необходимо разработать программный продукт – бота, который будет выполнять следующие действия:
	По введенным параметрам выполнять команды определения адресата по описанию входного документа, выдачи документов за определенный период по заданному адресату
	Распознавать команды, описанные на естественном языке, например, «Кому бы можно было направить письмо, в котором написано …»
	Предоставлять справку по имеющимся командам и их параметрам

4.2Настройки бота
Реализовать параметры «жесткости» определения адресата таким образом, чтобы пользователь мог устанавливать возможность выдачи одного конкретного адресата, либо нескольких наиболее вероятных, для заданного текста документа

4.3Подготовка руководства пользователя
Разработать руководство пользователя для бота, в котором описать интерфейс и возможности для потенциального пользователя

# Сессия 5

5.1 Разработка API
Разработайте интерфейс, позволяющий подключить разработанный программный продукт в качестве модуля к системе электронного документооборота. Интерфейс должен предоставлять метод или совокупность методов, принимающих в качестве параметров выдачу структуры данных СЭД «Практика». В качестве результата должна возвращаться аналогичная структура с заполненным значением (значениями) атрибута Адресат

5.2Последующее обучение
Для повышения точности сортировки корреспонденции в разработанный программный продукт необходимо внеси опцию оценки корректности результата. Если оператор системы считает, что адресат определен неправильно, он должен иметь возможность внести изменения. При каждой такой ситуации должен дополняться новый набор данных, который в перспективе можно будет использовать для обучения модели.

5.3Программная документация
Для разработанного APIсоставьте программную документацию

API (application programming interface) — это набор готовых классов, функций, процедур, структур и констант, предоставляемые самим приложением или операционной системой для взаимодействия с внешними программами.
Например, у вас есть кот Барсик, который любит лежать на обеденном столе. Вам это не нравится. Вы говорите Барсику: «Барсик, брысь со стола!». Барсик хоть и нехотя, но слезает со стола. Так вот, API — это набор команд, благодаря которым кот Барсик понял хозяина, что ему следует слезь со стола. Другой пример, если программу (модуль, библиотеку) рассматривать как чёрный ящик, то API — это множество «ручек», которые доступны пользователю данного ящика и которые он может вертеть и дёргать.
При этом пользователю необязательно понимать и знать, что такое API. API это «язык» общения между двумя программами и необходим программистам. API создаётся чтобы приложения созданные разными разработчикам корректно существовали вместе и могли взаимодействовать друг с другом. Компоненты образуют иерархию, в результате которой высокоуровневые компоненты используют API низкоуровневых компонентов, а те, в свою очередь, используют API ещё более низкоуровневых компонентов. По такому принципу построены протоколы передачи данных по Интернет. Каждый уровень пользуется функциональностью предыдущего («нижележащего») уровня и, в свою очередь, предоставляет нужную функциональность следующему («вышележащему») уровню.
На рисунке ниже представлена схема СЭД «Кодекс: Документооборот», в которой отображено API для внешних систем, а также для внутренних в данной СЭД.
Сигнатура функции
Сигнатура функции — это часть общего объявления функции, позволяющая средствам трансляции идентифицировать функцию среди других. В различных языках программирования существуют разные представления о сигнатуре функции, что также тесно связано с возможностями перегрузки функций в этих языках.
Например, в языке программирования C++ простая функция однозначно опознаётся компилятором по её имени и последовательности типов её аргументов, что составляет сигнатуру функции в этом языке. Если функция является методом некоторого класса, то в сигнатуре будет участвовать и имя класса.
В языке программирования Java сигнатуру метода составляет его имя и последовательность типов параметров; тип возвращаемого значения в сигнатуре не участвует.
В СЭД «Кодекс: Документооборот» используется API на основе web-технологий REST-API, на её примере рассмотрим формирование вызова любого GET\POST запроса.
Семантика функции
Семантика функции — это описание того, что данная функция делает. Семантика функции включает в себя описание того, что является результатом вычисления функции, как и отчего этот результат зависит. Обычно результат выполнения зависит только от значений аргументов функции, но в некоторых модулях есть понятие состояния. Полным описанием семантики функций является исполняемый код функции или математическое определение функции.
В API находится обученная модель которую можно использоваться :D
