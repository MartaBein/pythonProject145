#Marta Bein
#oqw417
#11320755
#CMPT-145-01 (41442.202305)


import node as n

def to_string(node_chain):
    """
    Purpose:
    Create a string representation of the node chain. E.g.,
    [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
    :param node_chain: A node-chain, possibly empty (None)
    Post_conditions:
    None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        return 'EMPTY'

    # walk along the chain
    walker = node_chain
    result = '[ {} |'.format(str(walker.get_data()))

    while walker.get_next() is not None:
        walker = walker.get_next()
        value = walker.get_data()
        # represent the next with an arrow-like figure
        result += ' *-]-->[ {} |'.format(str(value))

    # at the end of the chain, use '/'
    result += ' / ]'
    return result


# demonstration to_string
empty_chain = None
chain = N.node(1, N.node(2, N.node(3)))
print('empty_chain --->', to_string(empty_chain))
print('chain - - - - - - - - ->', to_string(chain))
