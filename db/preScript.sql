INSERT INTO public."Category" (id, name) VALUES ('7f5aaa9d-425c-43e5-8663-ea7a9ed2d41b', 'Celulares');
INSERT INTO public."Category" (id, name) VALUES ('81f5f835-361c-4f0c-b67b-134f40b82a8a', 'Videojuegos');

INSERT INTO public."Identifier_Type" (id, name) VALUES ('4b9c0754-68c4-49ef-bff2-5e7386cf557e', 'Cedula');

INSERT INTO public."Client" (id, id_identifier_type, identifier, name, email, password, location, credits) VALUES ('9c675160-c9a4-4d53-9194-9caf886510a8', '4b9c0754-68c4-49ef-bff2-5e7386cf557e', '1000515936', 'Jesús Leiva', 'jema0622@outlook.com', 'aas%daCQ9Fb@dQPUyF%2fhS?QfUzVp$fBDuHbpC?k^$quW-NVddP%*eFcZB_#hc=xT&pN2p3skH=gdnAAW2GgU?d&&Zq5Z+fmt#_tSX', 'Calle 16 # 10B - 60', 0);


INSERT INTO public."Product" (id, id_category, name, amount, description, cost) VALUES ('9e94bed2-37c4-4ee8-8d4a-4bf196c29bf4', '97a612a5-08ff-4f8b-a6b6-2829505f7aba', 'Tecno Mobile Pova 2', 100, 'Tecno Mobile Pova 2', 600000);
INSERT INTO public."Product" (id, id_category, name, amount, description, cost) VALUES ('3b29d445-92b5-4a66-bb20-d9c7bf3da201', '97a612a5-08ff-4f8b-a6b6-2829505f7aba', 'Iphone 9', 100, 'Iphone Plus 9 Sliver', 5000000);
INSERT INTO public."Product" (id, id_category, name, amount, description, cost) VALUES ('a83b8733-d394-4faa-b9e4-c20625099fbc', 'c99d64a7-2a87-432b-b129-5a965eeb2906', 'Resident Evil 5', 100, 'Juego Resident Evil 5', 60000);


INSERT INTO public."Transaction" (id, id_client, date, total) VALUES ('466b90ef-1485-4a8c-bf6d-2cbd1d06a0bf', '9c675160-c9a4-4d53-9194-9caf886510a8', '2021-10-12 10:18:12.018659', 600000);
INSERT INTO public."Transaction" (id, id_client, date, total) VALUES ('85cf5dc9-8dde-4d25-9b66-c969bb0cf9f5', '9c675160-c9a4-4d53-9194-9caf886510a8', '2021-10-12 10:20:30.020515', 5060000);

INSERT INTO public."Purchased" (id, id_transaction, id_product, amount, cost) VALUES ('2133d841-b967-4574-acec-3c44d2581346', '466b90ef-1485-4a8c-bf6d-2cbd1d06a0bf', '9e94bed2-37c4-4ee8-8d4a-4bf196c29bf4', 1, 600000);
INSERT INTO public."Purchased" (id, id_transaction, id_product, amount, cost) VALUES ('81d9eb32-2229-4038-8512-bba8d8d55dc0', '85cf5dc9-8dde-4d25-9b66-c969bb0cf9f5', '3b29d445-92b5-4a66-bb20-d9c7bf3da201', 1, 5000000);
INSERT INTO public."Purchased" (id, id_transaction, id_product, amount, cost) VALUES ('d6183ad1-6c4a-4b11-a068-e4dd83f8aeb3', '85cf5dc9-8dde-4d25-9b66-c969bb0cf9f5', 'a83b8733-d394-4faa-b9e4-c20625099fbc', 1, 60000);