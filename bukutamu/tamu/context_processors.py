def user_context(request):
    """
    Adds additional context to all templates
    """
    return {
        'is_admin': request.user.is_authenticated and request.user.role == 'admin',
        'site_name': 'Buku Tamu Django',
        'current_year': datetime.datetime.now().year,
    } 