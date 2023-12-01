def aplicar_filtro(queryset, filtro):
    # Filtro por nombre
    if filtro == 'asc':
        return queryset.order_by('titulo')
    elif filtro == 'des' :
        return queryset.order_by('-titulo')

    # Filtrar por elemento
    if filtro == 'Venus':
        return queryset.filter(elemento = 'Venus')
    elif filtro == 'Marte':
        return queryset.filter(elemento = 'Marte')
    elif filtro == 'Jupiter':
        return queryset.filter(elemento = 'Jupiter')
    elif filtro == 'Mercurio':
        return queryset.filter(elemento = 'Mercurio')

    # Filtro por tipo de item
    if filtro == 'ataque':
        return queryset.filter(tipo_item = 'ataque')
    elif filtro == 'defensa':
        return queryset.filter(tipo_item = 'defensa')
    elif filtro == 'forjable':
        return queryset.filter(tipo_item = 'forjable' )

    # Filtro por tipo de arma
    if filtro == 'espada_larga':
        return queryset.filter(tipo_arma = 'espada_larga')
    elif filtro == 'espada_corta':
        return queryset.filter(tipo_arma = 'espada_corta')
    elif filtro == 'baston':
        return queryset.filter(tipo_arma = 'baston')

    if filtro == 'golden_sun':
        return queryset.filter(juego = 'golden_sun')
    elif filtro == 'golde_sun_2':
        return queryset.filter(juego = 'golden_sun_2')

    return queryset.all()

def aplicar_filtros_dinamicos(queryset, variable, filtro):
    # Para ascendente y descendente
    if variable == "nombre":
        if filtro == "titulo":
            return queryset.order_by('titulo')
        else:
            return queryset.order_by('-titulo')
    
    # Filtro con variables
    filtro_dinamico = {f"{variable}__icontains": filtro}
    return queryset.filter(**filtro_dinamico)