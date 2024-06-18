#from comunidadeimpressionadora import app, database
#from comunidadeimpressionadora.models import Usuario, Post
#with app.app_context():
 #   database.create_all()

#with app.app_context():
#    usuario_tst_1 = Usuario(username='Marcio', email='mcnascimento@gmail.com',senha='1234567')
#    usuario_tst_2 = Usuario(username='Jaque', email='jcnascimento@gmail.com',senha='1234567')
#    usuario_tst_3 = Usuario(username='Yasmin', email='akymigoto@gmail.com', senha='1234567')
#    database.session.add(usuario_tst_1)
#    database.session.add(usuario_tst_2)
#    database.session.add(usuario_tst_3)
#    database.session.commit()

#COMANDOS PARA PESQUISAR NO BD
# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print (meus_usuarios)
#
#     meus_usuarios2 = Usuario.query.first()
#     print(meus_usuarios2)
#
#     primeiro_usuario = meus_usuarios[0]
#     print(primeiro_usuario)
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.senha)
#     print(primeiro_usuario.posts)
#
#     usuario_teste = Usuario.query.filter_by(id=1).first()
#     print(usuario_teste)
#     print(usuario_teste.email)
#
#     usuario_teste2 = Usuario.query.filter_by(email='mcnascimento@gmail.com').first()
#     print(usuario_teste2)
#     print(usuario_teste2.username)
#
#     #meu_post = Post(id_usuario=1, titulo="Primeiro post do Marcio", corpo="Aula de python com banco de dados")
#     #database.session.add(meu_post)
#     #database.session.commit()
#
#     post = Post.query.all()
#     print(post)
#
#     post1 = Post.query.first()
#     print(post1.titulo)
#     print(post1.autor)
#     print(post1.autor.email)
#     print(post1.corpo)

#Para deletar tudo / zerar e recriar novamente:

# with app.app_context():
#      database.drop_all()
#      database.create_all()

