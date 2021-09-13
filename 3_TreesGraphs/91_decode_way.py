class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def numDecodings(s: str) -> int:
    n = len(s)
    if n < 1:
        # the str is empty
        return 0
    if n == 1:
        # 0 can't be decoded
        if s[0] == '0':
            return 0
        # other single characeter can be decoded
        else:
            return 1
    # create a queue to do BFS
    queue = []
    if s[0] == '0':
        return 0

    root = TreeNode(val=[s[0]])
    queue.append(root)
    # the end of one level
    queue.append('#')
    level = 0
    count = 0
    while queue is not None:
        node = queue.pop(0)

        if node == '#':
            if queue is None:
                break
            level = level + 1
            queue.append('#')
            continue
            

        
        vec_str_l = node.val.copy()
        vec_str_r = node.val.copy()

        if level + 1 > n - 1:
            break

        c = s[level+1]
        combine = vec_str_l[-1]+c
        if vec_str_l[-1] != '0' and int(combine) <= 26:
            vec_str_l.append(combine)
            node_left = TreeNode(vec_str_l)
            node.left = node_left
            queue.append(node_left)
            if level == n-2:
                count  = count + 1

        
        if c != '0':
            vec_str_r.append(c)
            node_right = TreeNode(vec_str_r)
            node.right = node_right
            queue.append(node_right)
            if level == n-2:
                count  = count + 1
        
    return count


if __name__ == '__main__':
    s = "11106"
    count = numDecodings(s)
        
