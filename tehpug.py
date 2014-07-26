# coding: utf-8
#
# ==========================================
# Developed by Mehdy Khoshnoody           =
# Contact @ mehdy.khoshnoody@gmail.com    =
# More info @ http://mehdy.net            =
# ==========================================
#
__author__ = 'mehdy'

import click

def version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('version 1.0')
    ctx.exit()

def validate(ctx, param, value):
    if value < 19:
        click.echo('You are not authoriazed to attend. you must be at least 18.')
        ctx.exit()
    else:
        return

@click.group()
@click.option('--version', callback=version, expose_value=False, is_flag=True, is_eager=True)
def main():
    '''
    This a detail section for the app
    '''
    pass

@main.command()
@click.option('--name', '-n', default='tehpug', type=click.STRING, help='enter your name')
@click.option('--age', '-a', default=15, callback=validate, help='enter your age')
@click.option('--attend/--not-attend', default=False)
@click.argument('out', type=click.File('w'), required=False)
@click.option('--group', type=click.Choice(['flask','django','click']), default='flask')
def pug(name, age, attend, out, group):
    '''
    this a help message for pug
    '''
    if out:
        if not attend:
            click.echo('Why???', out)
        click.echo('hello %s, you are %s years old.\nwelcome to PUG' %(name, age), out)
        click.echo('you are member of %s subgroup in pug.' %group, out)
    else:
        if not attend:
            click.echo('Why???')
        click.echo('hello %s, you are %s years old.\nwelcome to PUG' % (name, age))
        click.echo('you are member of %s subgroup in pug.' % group)


@main.command()
@click.option('--name', '-n', default='tehpug', type=click.STRING, help='enter your name')
@click.option('--age', '-a', default=15, help='enter your age')
def lug(name, age):
    '''
    and a help message for lug
    '''
    click.echo('hello %s, you are %s years old.\nwelcome to LUG' %(name, age))