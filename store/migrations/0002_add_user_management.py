from django.db import migrations

# Generated by Django 5.0.3 on 2024-04-03 12:44


def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    # Create the 'Product Moderation' group
    product_moderation_group, _ = Group.objects.get_or_create(name="Product Moderation")

    # Assign appropriate permissions to the 'Product Moderation' group
    product_moderation_permissions = [
        "add_product",
        "view_product",
        "change_product",
        "delete_product",
    ]
    for permission in product_moderation_permissions:
        permission_obj = Permission.objects.get(codename=permission)
        product_moderation_group.permissions.add(permission_obj)

    # Create the 'Page Moderation' group
    page_moderation_group, _ = Group.objects.get_or_create(name="Page Moderation")

    # Assign appropriate permissions to the 'Page Moderation' group
    page_moderation_permissions = [
        "add_shop",
        "view_shop",
        "change_shop",
        "delete_shop",
        "add_category",
        "view_category",
        "change_category",
        "delete_category",
        "add_product",
        "view_product",
        "change_product",
        "delete_product",
        "add_productimage",
        "view_productimage",
        "change_productimage",
        "delete_productimage",
    ]
    for permission in page_moderation_permissions:
        permission_obj = Permission.objects.get(codename=permission)
        page_moderation_group.permissions.add(permission_obj)


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
        ("auth", "0001_initial"),  # Add the 'auth' app as a dependency
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
