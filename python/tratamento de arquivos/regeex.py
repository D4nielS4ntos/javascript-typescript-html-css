import os
import re


# texto += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur id erat vel massa auctor dictum quis vitae sem. Donec maximus nisl tellus, vel hendrerit erat efficitur vitae. Donec eu est ex. Nam venenatis elit laoreet, sodales augue id, porttitor lorem. Nam sagittis mauris a nisl finibus, nec semper mauris tempus. In hac habitasse platea dictumst. Sed consectetur scelerisque leo, sed venenatis erat malesuada rutrum. Phasellus ut tincidunt velit. Donec tincidunt justo pulvinar accumsan semper. Quisque odio augue, pulvinar aliquam gravida vitae, scelerisque ac neque. Ut at porta elit. Morbi sed enim eu ex gravida mollis a egestas quam. Nam et rutrum justo. Nunc commodo, lorem ut scelerisque tempus, est dui egestas mi, id sodales neque ex quis lacus.'
# texto += 'Curabitur at ultricies lectus. Morbi ipsum tortor, ullamcorper id arcu ac, lacinia ultrices augue. Aenean et tellus velit. Mauris finibus quis elit non tincidunt. Vivamus ac lacus est. Nam interdum, purus id egestas lacinia, augue enim sollicitudin purus, consequat pellentesque ligula est at risus. Nam sagittis commodo diam pulvinar volutpat. Vestibulum lorem ante, tempor sed tincidunt ut, eleifend sit amet nibh. Duis malesuada felis ut ipsum dapibus efficitur. Pellentesque quis euismod dolor. Mauris sed ornare nisi.'
# texto += 'Pellentesque ullamcorper elementum imperdiet. Aenean nibh ante, tincidunt in mattis eu, dapibus sed lectus. Duis nisi lectus, malesuada ut efficitur ut, ultricies ac nibh. Sed iaculis id ipsum et consequat. Donec odio ex, feugiat pellentesque placerat sit amet, facilisis id lectus. Vivamus lacus dolor, accumsan a eleifend in, mattis eget odio. Donec vitae rutrum justo. Donec congue volutpat mauris, non mattis ligula pharetra id.'
# texto += 'Maecenas convallis ornare orci, id mollis magna ultricies vitae. Mauris semper quis mi vel pretium. Fusce vel venenatis velit. Curabitur vitae porta libero. Pellentesque sit amet sodales arcu. Nunc mattis sem vitae nisl volutpat, id maximus leo aliquam. Curabitur non libero finibus, maximus nunc at, euismod nisi.'
# texto += 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur lacinia tempus tempus. Quisque quam nulla, commodo nec ante quis, rutrum facilisis magna. Duis sed varius augue. Fusce a eros porttitor, mattis nisl egestas, convallis nisi. Fusce ac ultricies dolor. Aliquam sed mi enim. Mauris nec ante dictum, mollis elit ut, laoreet risus. Phasellus interdum tristique erat eu imperdiet. Suspendisse volutpat vel elit sed egestas. In imperdiet pharetra mauris nec semper. Nullam feugiat ullamcorper posuere. In vestibulum congue felis, sit amet porttitor tortor placerat non. Nulla interdum, nisi a bibendum pharetra, mi lacus commodo lacus, sit amet tincidunt mi urna et lorem. Maecenas condimentum ex fringilla, faucibus augue vel, convallis massa. Fusce eleifend, dui et faucibus egestas, ex metus convallis augue, tempus porta orci odio non erat.'

os.system('cls')
while True:

    texto = open('lorem_ipsum.txt', 'r')
    texto = texto.read()

    pesquisa = input('Digite o que quer pesquisar: ')
    
    resultado = re.findall(pesquisa, texto)
    posicao = re.search(pesquisa, texto)
    texto_quebrado = re.split(pesquisa, texto)

    print(resultado)
    print(f'{pesquisa} len: {len(resultado)}\n')
    print(f'{pesquisa} start: {posicao.start()}\n')
    print(f'{pesquisa} end: {posicao.end()}\n')

    substituir = input('Digite o que quer substituir: ')

    texto_substituido = re.sub(pesquisa, substituir, texto)

    print(f'"{pesquisa}" texto quebrado: {texto_substituido}\n')

    substituir = input('Continuar? ')
    os.system('cls')
